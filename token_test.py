from google import genai

# 1. Active Client Engine connect karna
client = genai.Client(api_key='AQ.Ab8RN6KfOIXqm2H8VtlDybJIn6mcNxEcYpTCmPAgRGhWX-PSVA')

# 2. Ek sample text file stream banana
sample_text = "Proficient in Python programming and structural database query configurations."

print("Analyzing token counts inside pipeline...")

# 3. Google Gemini ke built-in token counter tool ko call karna
token_analysis = client.models.count_tokens(
    model='gemini-3.8-flash',
    contents=sample_text
)

# 4. Result ko screen par print karna
print("\n--- TOKEN LOGICS REPORT ---")
print("Total Words written:", len(sample_text.split()))
print("Total Tokens calculated by AI:", token_analysis.total_tokens)
