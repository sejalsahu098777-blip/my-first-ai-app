import os
from dotenv import load_dotenv  # Secret file manager module bulaya
from google import genai

# 1. Background me chhupi hui .env file ko load karna
load_dotenv()

# 2. Operating System (os) se bolna ki environment se chabi nikal kar laaye
SECURE_KEY = os.getenv("GEMINI_API_KEY")

print("--- SECURITY ENGINE METRICS ---")
print("Extracted Key Preview from Background:", SECURE_KEY[:10] + "...")

# 3. Connection initialisation bina khule aam password likhe!
client = genai.Client(api_key=SECURE_KEY)

response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents="Output exactly one word: 'Secure'"
)

print("Model Verification Status:", response.text)
