# 🤖 Gemini Chatbot with FastAPI, RAG & FAISS

This project is a **Gemini-powered chatbot** built step-by-step with validation, backend integration, and Retrieval Augmented Generation (RAG).  
It collects user details, validates inputs, stores data, and uses a vector database to retrieve relevant information.

The project demonstrates the **end-to-end workflow of building an AI chatbot**, starting from a static interface to a fully dynamic RAG-powered system.

---

# 🚀 Features

- Gemini AI chatbot integration using Google AI Studio API
- Input validation for user details
- Dynamic backend using FastAPI
- JSON file data storage
- Retrieval-Augmented Generation (RAG)
- FAISS vector database
- Sentence-transformer embeddings
- Structured conversation flow

---

# 📌 Tech Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- FastAPI (Python)

### AI / ML
- Gemini API (Google AI Studio)
- Sentence Transformers
- RAG Architecture

### Vector Database
- FAISS (IndexFlatL2)

### Embedding Model
- `all-MiniLM-L6-v2`

---

# 📂 Project Workflow

This chatbot was developed in **multiple steps**:

---

## Step 1 — Static Implementation

- Created a basic chatbot UI
- Collected user information:
  - Name
  - Email
  - Mobile Number
- Implemented input validations:
  - **Mobile number:** Only 10 digits allowed
  - **Email:** Must follow format like `example@gmail.com`
- Added conversation flow
- Displays **"Thank You"** message at the end

---

## Step 2 — Gemini Integration

Integrated **Gemini model** using API from Google AI Studio.

The chatbot can now:
- Generate AI responses
- Handle conversation dynamically
- Use Gemini for answering user queries

---

## Step 3 — Dynamic Backend with FastAPI

Converted the chatbot into a **dynamic application**.

Added:
- FastAPI backend
- API endpoints
- JSON file storage for chatbot data

User data and conversation logs are stored in a **JSON file**.

---

## Step 4 — Retrieval-Augmented Generation (RAG)

Implemented **RAG pipeline** to improve chatbot responses.

Components used:

### Embedding Model

all-MiniLM-L6-v2


### Vector Database
FAISS
IndexFlatL2


### Workflow:

1. Convert documents into embeddings
2. Store embeddings in FAISS vector index
3. Retrieve relevant context
4. Send retrieved context to Gemini
5. Generate accurate responses

This improves the chatbot's **context awareness and answer quality**.

---


---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/shauryachawla15/gGEMINI-chatbot.git

cd gemini-chatbot


# ▶️ Run the Project

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Open in your browser:

```
http://127.0.0.1:8000
```

---

# 💬 Validation Rules

### Mobile Number
- Must be **10 digits**
- Only numeric characters allowed

Example:

```
9876543210
```

### Email

Must follow format:

```
example@gmail.com
```

---

# 🧠 RAG Pipeline

The RAG system works as follows:

```
User Query
    ↓
Embedding Generation
    ↓
FAISS Vector Search
    ↓
Relevant Context Retrieved
    ↓
Gemini Model
    ↓
Final AI Response
```

This architecture helps the chatbot provide **more relevant and accurate answers**.

---

# 📊 Learning Outcomes

Through this project I learned:

- Building AI chatbots
- Integrating Gemini API
- FastAPI backend development
- Input validation techniques
- JSON data storage
- Vector databases (FAISS)
- Embedding models
- Retrieval-Augmented Generation (RAG)

---

# 🔮 Future Improvements

- Database integration (MongoDB / PostgreSQL)
- Authentication system
- UI improvements
- Deployment on cloud
- Streaming responses
- Memory-based conversations

---

# 🙌 Acknowledgements

- Google AI Studio (Gemini API)
- Sentence Transformers
- FAISS
- FastAPI

---

# 📜 Output

<img width="1920" height="1080" alt="Screenshot (1)" src="https://github.com/user-attachments/assets/90407603-209a-40f9-91d4-9e036d847a2b" />
<img width="1920" height="1080" alt="Screenshot (3)" src="https://github.com/user-attachments/assets/e2a885e6-d504-45a7-8816-9e87c7c31610" />
<img width="1920" height="1080" alt="Screenshot (4)" src="https://github.com/user-attachments/assets/b3e6673e-9b71-4867-bcbd-82b8ad847deb" />
<img width="1920" height="1080" alt="Screenshot (5)" src="https://github.com/user-attachments/assets/39cd2da0-ed1f-4482-a3e2-e7de139de777" />


---

⭐ If you like this project, consider giving it a **star on GitHub!**
