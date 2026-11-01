import streamlit as st
from google import genai
from google.genai import types
from pypdf import PdfReader

# 1. Structural Elite Page Config
st.set_page_config(
    page_title="Enterprise Profile Auditor", 
    page_icon="🎯", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Premium Neon-Slate CSS Injection
st.markdown("""
    <style>
    .stApp { background-color: #0F172A; color: #E2E8F0; }
    [data-testid="stMetricValue"] { font-size: 40px; color: #38BDF8 !important; font-weight: 700; }
    [data-testid="stMetricLabel"] { color: #94A3B8 !important; font-size: 16px; }
    .stButton>button {
        background: linear-gradient(135deg, #38BDF8 0%, #0284C7 100%) !important;
        color: white !important; border: none !important; padding: 12px 24px !important;
        border-radius: 8px !important; font-weight: bold !important; transition: all 0.3s ease;
    }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(56, 189, 248, 0.4); }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #38BDF8;'>🚀 Enterprise AI Profile Auditor & Match Engine</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 16px; color: #94A3B8;'>Optimized High-Speed Streaming Pipeline Running Gemini 3.8 Flash SDK</p>", unsafe_allow_html=True)
st.markdown("<hr style='border-color: #1E293B;'>", unsafe_allow_html=True)

# 2. FIXED ISSUE 1: Sidebar Console with Dynamic Custom Role Selection Menu
st.sidebar.markdown("<h3 style='color: #38BDF8;'>🏢 Deployment Console</h3>", unsafe_allow_html=True)
role_options = ["Junior AI Engineer", "Python Developer", "Data Solutions Engineer", "AI Solutions Engineer", "Data Engineer", "Other (Type Custom Role)"]
selected_option = st.sidebar.selectbox("Target Job Designation:", role_options)

# Agar user 'Other' select karega, toh custom text input active ho jayega
if selected_option == "Other (Type Custom Role)":
    target_role = st.sidebar.text_input("Enter your custom target role:", placeholder="e.g. Flutter Developer")
else:
    target_role = selected_option

st.sidebar.markdown("<hr style='border-color: #1E293B;'>", unsafe_allow_html=True)

# 3. Connection pipeline setup
client = genai.Client(api_key='AQ.Ab8RN6KfOIXqm2H8VtlDybJIn6mcNxEcYpTCmPAgRGhWX-PSVA')

# 4. Interface Grid Elements
col1, col2 = st.columns(2)
with col1:
    st.markdown("<h4 style='color: #38BDF8;'>📁 Ingestion Layer</h4>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Drop professional PDF template instance here:", type=["pdf"])
with col2:
    st.markdown("<h4 style='color: #38BDF8;'>⚙️ Execution Controls</h4>", unsafe_allow_html=True)
    st.write("Trigger real-time responsive analytics token routing:")
    analyze_btn = st.button("Execute Pipeline Inference", use_container_width=True)

# 5. Live Architecture Pipeline
if analyze_btn:
    if uploaded_file is not None and target_role:
        # Dynamic interface placement containers for streaming values
        metric_placeholder = st.empty()
        st.markdown("<h3 style='color: #38BDF8;'>📊 Real-Time Report Diagnostics Dashboard</h3>", unsafe_allow_html=True)
        
        tab1, tab2 = st.tabs(["📋 Analysis Overview Logs", "⚡ High-Yield Interview Simulation"])
        
        with st.spinner("Extracting content segments and initializing streaming cluster..."):
            reader = PdfReader(uploaded_file)
            user_skills = ""
            for page in reader.pages:
                text = page.extract_text()
                if text: user_skills += text + "\n"
        
        if len(user_skills.strip().split()) < 10:
            st.error("Error: Token extraction boundaries failed.")
        else:
            prompt_payload = f"Target Role: {target_role}\nCandidate Profile: {user_skills}"
            
            # Strict structural layout rules
            config = types.GenerateContentConfig(
                system_instruction=(
                    "You are a Principal AI Architect and Technical Recruiter. "
                    "Analyze the provided Candidate Profile against the Target Role. "
                    "You must structure your output exactly using the tag [SPLIT_HERE] to separate sections.\n\n"
                    "Format your response exactly like this:\n"
                    "SCORE: [Only output a single number score out of 100, e.g. 85]\n"
                    "CRITIQUE: [Provide exactly a 2-sentence structural critique identifying technological alignment or discrepancies.]\n"
                    "[SPLIT_HERE]\n"
                    "### TARGETED INTERVIEW QUESTIONS\n"
                    "[Provide exactly 3 highly specific technical questions testing enterprise capabilities.]"
                )
            )
            
            # FIXED ISSUE 2: Switching to high-speed stream generation pipeline
            # Isse text token compute hote hi screen par real-time type hone lagega!
            response_stream = client.models.generate_content_stream(
                model='gemini-3.8-flash',
                contents=prompt_payload,
                config=config
            )
            
            full_raw_text = ""
            with tab1:
                st.info("Live Evaluation Log Stream:")
                text_placeholder = st.empty()
                
                # Dynamic stream block accumulation loop
                for chunk in response_stream:
                    full_raw_text += chunk.text
                    text_placeholder.markdown(full_raw_text)
            
            # Stream extraction final split cleanup processing
            if "[SPLIT_HERE]" in full_raw_text:
                parts = full_raw_text.split("[SPLIT_HERE]")
                rating_block = parts[0].strip()
                questions_block = parts[1].strip()
                
                score_num = "N/A"
                for line in rating_block.split("\n"):
                    if "SCORE:" in line:
                        score_num = line.replace("SCORE:", "").strip()
            else:
                rating_block = full_raw_text
                questions_block = "Extraction format parsing shift. View full log in Tab 1."
                score_num = "Completed"
            
            # Updating UI cards after tokens settle down
            with metric_placeholder.container():
                st.metric(label=f"🎯 Target Fit: {target_role}", value=f"{score_num} %")
                
            with tab2:
                st.subheader("Strict Evaluation Mock Drills")
                st.write(questions_block)
                
            st.success("Pipeline Analysis Core Optimization Complete!")
    else:
        st.sidebar.error("Execution aborted: Ensure a valid file is loaded and a custom job role target is specified.")
