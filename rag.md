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
