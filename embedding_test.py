import os
import chromadb
from dotenv import load_dotenv
from google import genai

# 1. Environment keys framework parsing
load_dotenv()
SECURE_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=SECURE_KEY)

print("--- LOCAL VECTOR DATABASE INITIALIZATION ---")

# 2. CORE CHROMA INSTANCE: Local database setup
chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="my_ai_storage")

# 3. TEXT CHUNK TO EMBEDDING PIPELINE
text_content = "Python programming pipelines manage automation."

analysis_vector = client.models.embed_content(
    model='gemini-embedding-001',
    contents=text_content
)

# FIXED CORE HOOK: Accessing values safely from the first index of the embeddings list array
real_vectors = analysis_vector.embeddings[0].values

# 4. DATABASE INGESTION LAYER: Storing inside local ChromaDB
collection.add(
    embeddings=[real_vectors], # 3072 numbers structure array list
    documents=[text_content],  # Original clean text text chunk
    ids=["id_chunk_001"]       # Unique ID for storage tracking
)

print("\n🚀 Ingestion Complete: Vector numbers safely stored inside ChromaDB data cluster!")
print("Stored Item Tracking ID:", collection.peek()['ids'])
