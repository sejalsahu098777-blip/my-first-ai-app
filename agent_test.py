import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

print("--- AI AGENT PIPELINE INITIALIZATION ---")
# 1. Background se secure environment variables load karna
load_dotenv()

# 2. Connection client structure config ready karna
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

print("Secure Connection Client Active!")
