from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. Ek bada complex continuous text dataset create kiya
heavy_enterprise_text = (
    "Applied AI Engineering requires deep core python comprehension. "
    "Data pipeline infrastructures safely isolate model schemas from drift. "
    "Vector embeddings manage search indexing inside scalable databases efficiently."
)

print("Initializing LangChain Automated Chunking Cluster...")

# 2. CORE CONFIGURATION: Chunk Size aur Overlap parameters set kiye
# chunk_size=60 -> Max 60 character ka ek dabba hoga
# chunk_overlap=15 -> Har agle dibbe me pichle wale ke 15 characters repeat honge
splitter = RecursiveCharacterTextSplitter(
    chunk_size=60,
    chunk_overlap=15,
    length_function=len
)

# 3. Text ko process karke safe list documents me transform karna
split_documents = splitter.split_text(heavy_enterprise_text)

print("\n--- OPTIMIZED OVERLAPPING CHUNKS ---")

# 4. Saare generated safe chunks ko print karne ka loop
for position, chunk in enumerate(split_documents):
    print(f"Secure Chunk [{position}]: {chunk}")
