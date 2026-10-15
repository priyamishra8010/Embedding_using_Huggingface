# this will create sentence into vectors 
# from langchain_huggingface import HuggingFaceEmbeddings

# embedding= HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# text="delhi is the capital of india"

# vector=embedding.embed_query(text)

# print(str(vector))
# print("Vector length = ",len(vector))




from langchain_huggingface import HuggingFaceEmbeddings

embedding1=HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")

document=[
    "what is AI?",
    "what is Machine Learning?",
    "what is Vector?"
]
vector=embedding1.embed_documents(document)

print(str(vector))
print("Vector length = ",len(vector))
