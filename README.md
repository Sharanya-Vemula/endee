# 🔍 Vector Debugger using Endee (Semantic Error Resolution System)

## 🚀 Project Overview

Debugging is a repetitive and time-consuming process for developers. Traditional search methods fail to capture the semantic meaning of errors and often return irrelevant results.

This project introduces a **Vector Debugger System** that uses semantic similarity and vector search to identify similar past debugging cases and recommend solutions.

It leverages **Endee Vector Database** to store and retrieve debugging knowledge efficiently.

---

## ❗ Problem Statement

Developers often struggle to resolve errors quickly because:
- Error messages are ambiguous  
- Traditional keyword search lacks context  
- Similar past issues are not effectively reused  

There is a need for a system that can understand the *meaning* of errors and suggest relevant fixes intelligently.

---

## 💡 Solution

We build an AI-powered debugging assistant that:

1. Converts error messages and code snippets into embeddings  
2. Stores them in a vector database (Endee)  
3. Performs semantic similarity search for new errors  
4. Retrieves similar debugging cases  
5. Suggests fixes with confidence scores  

This enables faster and smarter debugging workflows.

---

## 🏗️ System Architecture
User Input (Error + Code)
↓
Embedding Model (Sentence Transformers)
↓
Endee Vector Database
↓
Top-K Similar Debug Cases
↓
Fix Recommendation Engine
↓
Response (Fix + Cause + Confidence)

---

## 🛠️ Tech Stack

- Python  
- FastAPI (Backend API)  
- Sentence Transformers (Embeddings)  
- Endee (Vector Database)  
- NumPy (Similarity computation)  

---

## 🧠 How Endee is Used

Endee is used as the core vector database for storing and retrieving debugging knowledge.

- Each debugging case (error + code) is converted into a vector embedding  
- These embeddings are stored in the Endee vector database  
- When a new error is received, it is converted into a vector  
- Semantic similarity search is performed to retrieve the most relevant past cases  

This enables context-aware debugging instead of simple keyword matching.

---

## ✨ Features

- Semantic error search using embeddings  
- Retrieval of similar debugging cases  
- Multiple solution suggestions  
- Confidence scoring system  
- FastAPI-based backend for real-time usage  

---

## 🔗 API Usage

### Endpoint:
POST /debug

### Request:
```json
{
  "error": "KeyError: user_id",
  "code": "df['user_id']"
}
```

##Response:
```json
{
  "solutions": [
    {
      "fix": "Check column names using df.columns",
      "cause": "Column does not exist",
      "confidence": 0.85
    }
  ],
  "overall_confidence": 0.85,
  "similar_cases_found": 3,
  "explanation": "Results are based on semantically similar past debugging cases using vector search."
}
```

## ⚙️ Setup Instructions
Clone the repository:
```
git clone https://github.com/Sharanya-Vemula/endee.git
cd endee
```
Create virtual environment:
```
python -m venv venv
venv\Scripts\activate
```
Install dependencies:
```
pip install -r requirements.txt
```
Run the server:
```
python -m uvicorn backend.main:app --reload
```
Open in browser:
```
http://127.0.0.1:8000/docs
```
## 🚀 Future Improvements
Integration with real-time debugging logs
LLM-based explanation generation
Support for multiple programming languages
Integration with IDEs (VS Code extension)

## 🎯 Conclusion

This project demonstrates how vector databases like Endee can be used as semantic memory systems for debugging workflows, enabling faster and more intelligent error resolution.


---

## 🚀 AFTER PASTING

Run:

```bash
git add README.md
git commit -m "Added README"
git push origin master
```
