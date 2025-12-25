```python
from flask import Flask
import pandas as pd
import faiss
from sentence_transformers import SentenceTransformer
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

# ----------------------------
# Gemini Setup
# ----------------------------
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
llm = genai.GenerativeModel("gemini-2.5-flash")

# ----------------------------
# Load CSV
# ----------------------------
df = pd.read_csv("qa_data (1).csv")
docs = [f"Q: {q}\nA: {a}" for q, a in zip(df.question, df.answer)]

# ----------------------------
# Embeddings + FAISS
# ----------------------------
embedder = SentenceTransformer("all-MiniLM-L6-v2")
emb = embedder.encode(docs)

index = faiss.IndexFlatL2(emb.shape[1])
index.add(emb)

# ----------------------------
# RAG Function
# ----------------------------
def rag(query):
    _, idx = index.search(embedder.encode([query]), 1)
    context = docs[idx[0][0]]

    prompt = f"""
Answer ONLY from the context below.
If not found, say: No relevant Q&A found.

Context:
{context}

Question: {query}
"""
    return llm.generate_content(prompt).text.strip()

# ----------------------------
# Simple User Input Loop
# ----------------------------
if __name__ == "__main__":
    print("🔍 RAG Q&A System (type 'exit' to quit)\n")

    while True:
        query = input("Ask your question: ")

        if query.lower() == "exit":
            print("👋 Exiting...")
            break

        answer = rag(query)

        print("\nAnswer:")
        print(answer)
        print("-" * 40)



```

```python
from flask import Flask, render_template, request
import pandas as pd
import faiss
from sentence_transformers import SentenceTransformer
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

app = Flask(__name__)

# ----------------------------
# Gemini Setup
# ----------------------------
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
llm = genai.GenerativeModel("gemini-2.5-flash")

# ----------------------------
# Load CSV
# ----------------------------
df = pd.read_csv("qa_data (1).csv")
docs = [f"Q: {q}\nA: {a}" for q, a in zip(df.question, df.answer)]

# ----------------------------
# Embeddings + FAISS
# ----------------------------
embedder = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = embedder.encode(docs)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# ----------------------------
# RAG Function
# ----------------------------
def rag(query):
    _, idx = index.search(embedder.encode([query]), 1)
    context = docs[idx[0][0]]

    prompt = f"""
Answer ONLY from the context below.
If not found, say: No relevant Q&A found.

Context:
{context}

Question: {query}
"""
    return llm.generate_content(prompt).text.strip()

# ----------------------------
# Flask Route
# ----------------------------
@app.route("/", methods=["GET", "POST"])
def home():
    answer = ""
    if request.method == "POST":
        query = request.form["query"]
        answer = rag(query)

    return render_template("index.html", answer=answer)

# ----------------------------
# Run App
# ----------------------------
if __name__ == "__main__":
    app.run(debug=True)


```


## html
```python

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>📄 RAG Chatbot</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
<style>
    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
        font-family: 'Inter', sans-serif;
    }
    body {
        background: linear-gradient(135deg, #74ebd5, #acb6e5);
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
        padding: 20px;
    }
    .chatbox {
        background: #fff;
        width: 100%;
        max-width: 600px;
        border-radius: 20px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.2);
        padding: 30px;
        display: flex;
        flex-direction: column;
        transition: transform 0.3s ease;
    }
    .chatbox:hover {
        transform: translateY(-5px);
    }
    h2 {
        text-align: center;
        color: #333;
        margin-bottom: 25px;
    }
    form {
        display: flex;
        flex-direction: column;
    }
    input[type="text"] {
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #ccc;
        font-size: 16px;
        margin-bottom: 15px;
        transition: all 0.3s ease;
    }
    input[type="text"]:focus {
        outline: none;
        border-color: #6c63ff;
        box-shadow: 0 0 10px rgba(108,99,255,0.3);
    }
    button {
        padding: 15px;
        border: none;
        border-radius: 12px;
        background: #6c63ff;
        color: #fff;
        font-size: 16px;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    button:hover {
        background: #574bff;
        transform: scale(1.05);
    }
    .answer {
        margin-top: 20px;
        background: #f0f4ff;
        border-left: 5px solid #6c63ff;
        padding: 20px;
        border-radius: 12px;
        font-size: 15px;
        color: #333;
        line-height: 1.5;
        animation: fadeIn 0.5s ease-in-out;
    }
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(10px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    @media (max-width: 640px) {
        .chatbox {
            padding: 20px;
        }
    }
</style>
</head>
<body>
<div class="chatbox">
    <h2>📄 CSV-based RAG Chatbot</h2>
    <form method="POST">
        <input type="text" name="query" placeholder="Ask me anything..." required>
        <button type="submit">Ask</button>
    </form>

    {% if answer %}
    <div class="answer">
        <strong>Answer:</strong><br>
        {{ answer }}
    </div>
    {% endif %}
</div>
</body>
</html>

```
