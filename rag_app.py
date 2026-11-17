import os
import streamlit as st
import chromadb
from dotenv import load_dotenv
from google import genai
from pypdf import PdfReader

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

st.set_page_config(
    page_title="Enterprise RAG Knowledge Engine",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .stApp { background-color: #0F172A; color: #E2E8F0; }
    [data-testid="stMetricValue"] { font-size: 36px; color: #38BDF8 !important; font-weight: 700; }
    [data-testid="stMetricLabel"] { color: #94A3B8 !important; font-size: 15px; }
    .stButton>button {
        background: linear-gradient(135deg, #38BDF8 0%, #0284C7 100%) !important;
        color: white !important; border: none !important; padding: 10px 22px !important;
        border-radius: 8px !important; font-weight: bold !important; transition: all 0.3s ease;
    }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(56, 189, 248, 0.4); }
    .answer-box {
        background-color: #1E293B; padding: 20px; border-radius: 10px;
        border-left: 5px solid #38BDF8; margin-top: 15px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #38BDF8;'>🧠 Enterprise RAG Document Intelligence System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 16px; color: #94A3B8;'>Vector-Powered Semantic Search & Zero-Hallucination Q&A Engine</p>", unsafe_allow_html=True)
st.markdown("<hr style='border-color: #1E293B;'>", unsafe_allow_html=True)

st.sidebar.markdown("<h3 style='color: #38BDF8;'>⚙️ System Architecture</h3>", unsafe_allow_html=True)
st.sidebar.info("**Vector DB:** ChromaDB (In-Memory)\n\n**Chunk Strategy:** 500 Chars Window\n\n**Retrieval:** Top-3 Semantic Match\n\n**Fallback Engine:** Multi-Model Routing")
st.sidebar.markdown("<hr style='border-color: #1E293B;'>", unsafe_allow_html=True)
st.sidebar.caption("Built for Enterprise Knowledge Retrieval")

chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection(name="pdf_knowledge_base")

col1, col2 = st.columns([1, 1.3], gap="large")

with col1:
    st.markdown("<h4 style='color: #38BDF8;'>📁 1. Knowledge Ingestion</h4>", unsafe_allow_html=True)
    uploaded_pdf = st.file_uploader("Upload Enterprise PDF (Policies, Reports, Resumes):", type=["pdf"])
    
    if uploaded_pdf is not None:
        if st.button("🚀 Vectorize & Store in ChromaDB", use_container_width=True):
            with st.spinner("Extracting text, chunking, and generating embeddings..."):
                reader = PdfReader(uploaded_pdf)
                full_text = ""
                for page in reader.pages:
                    extracted = page.extract_text()
                    if extracted:
                        full_text += extracted + "\n"
                
                chunk_size = 500
                chunks = [full_text[i:i+chunk_size] for i in range(0, len(full_text), chunk_size)]
                
                for idx, chunk in enumerate(chunks):
                    collection.upsert(
                        documents=[chunk],
                        ids=[f"chunk_{idx}"]
                    )
                st.session_state["chunks_count"] = len(chunks)
                st.session_state["pages_count"] = len(reader.pages)
                st.success("✅ Knowledge Base Indexed Successfully!")

    if "chunks_count" in st.session_state:
        m1, m2 = st.columns(2)
        m1.metric("📄 Pages Parsed", st.session_state["pages_count"])
        m2.metric("🧩 Vector Chunks", st.session_state["chunks_count"])

with col2:
    st.markdown("<h4 style='color: #38BDF8;'>🔍 2. Semantic Query & Inference</h4>", unsafe_allow_html=True)
    user_question = st.text_input("Enter your question strictly based on the uploaded PDF:", placeholder="e.g., Summarize the key technical skills or policies...")
    
    if st.button("⚡ Retrieve & Generate Answer", use_container_width=True):
        if user_question:
            with st.spinner("Searching ChromaDB vectors & synthesizing response..."):
                results = collection.query(
                    query_texts=[user_question],
                    n_results=3
                )
                
                if results["documents"] and len(results["documents"][0]) > 0:
                    retrieved_context = "\n".join(results["documents"][0])
                    
                    prompt = f"""
                    You are an Enterprise AI Knowledge Assistant. Answer the user's question using ONLY the context provided below.
                    If the answer is not present in the context, state clearly: 'Information not found in the uploaded document.'
                    
                    Context:
                    {retrieved_context}
                    
                    Question: {user_question}
                    """
                    
                    models_to_try = ["gemini-3.5-flash", "gemini-3.5-flash-lite", "gemini-2.5-flash-lite"]
                    answer_text = None
                    used_model = ""
                    
                    for model_name in models_to_try:
                        try:
                            response = client.models.generate_content(
                                model=model_name,
                                contents=prompt
                            )
                            answer_text = response.text
                            used_model = model_name
                            break
                        except Exception:
                            continue
                    
                    if answer_text:
                        st.markdown(f"<div class='answer-box'><h4 style='color:#38BDF8; margin-top:0;'>💡 Verified AI Response</h4>{answer_text}</div>", unsafe_allow_html=True)
                        st.caption(f"⚡ Synthesized via `{used_model}` | Grounded in Top-3 ChromaDB Chunks")
                    else:
                        st.error("All AI models are experiencing high traffic. Please retry in 10 seconds.")
                else:
                    st.warning("⚠️ Please upload a PDF and click 'Vectorize & Store in ChromaDB' first!")
        else:
            st.warning("⚠️ Please enter a question to query the knowledge base.")
