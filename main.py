from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from google import genai
import json
import os
import faiss
import numpy as np

app = FastAPI()

# Mount static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# 🔐 IMPORTANT: Move this to .env later
client = genai.Client(api_key="YOUR_API_KEY _HERE")


# ---------------------------
# Embedding Function
# ---------------------------
from sentence_transformers import SentenceTransformer

# Load once globally
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embedding(text):
    return embedding_model.encode(text)

# ---------------------------
#  Load Documents
# ---------------------------
DOCUMENT_FILE = "documents.txt"
INDEX_FILE = "faiss_index.bin"

with open(DOCUMENT_FILE, "r", encoding="utf-8") as f:
    documents = [line.strip() for line in f.readlines() if line.strip()]

dimension = len(get_embedding(documents[0]))

# ---------------------------
#  Build or Load FAISS Index
# ---------------------------
if os.path.exists(INDEX_FILE):
    index = faiss.read_index(INDEX_FILE)
else:
    embeddings = [get_embedding(doc) for doc in documents]
    embeddings = np.array(embeddings)

    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    faiss.write_index(index, INDEX_FILE)


# ---------------------------
#  Pydantic Model
# ---------------------------
class UserData(BaseModel):
    name: str
    email: str
    mobile: str
    query: str


# ---------------------------
#  Home Route
# ---------------------------
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# ---------------------------
#  Submit Route (RAG + JSON Storage)
# ---------------------------
@app.post("/submit")
async def submit(data: UserData):

    # -------- Save to JSON --------
    file_path = "data.json"

    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            json.dump([], f)

    with open(file_path, "r") as f:
        existing_data = json.load(f)

    existing_data.append(data.dict())

    with open(file_path, "w") as f:
        json.dump(existing_data, f, indent=4)

    # -------- RAG Retrieval --------
    query_embedding = get_embedding(data.query)

    D, I = index.search(np.array([query_embedding]), k=2)

    retrieved_docs = [documents[i] for i in I[0]]

    context = "\n".join(retrieved_docs)

    # -------- Gemini Generation --------
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=f"""
You are a helpful assistant. Answer using the provided context.

Context:
{context}

Question:
{data.query}
"""
    )

    ai_reply = response.text


    return JSONResponse(content={"message": ai_reply})
