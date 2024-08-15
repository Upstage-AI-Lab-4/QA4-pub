from langchain_upstage import UpstageEmbeddings
from langchain_chroma import Chroma
import os

def create_vector_store(documents):
    embeddings = UpstageEmbeddings(
        api_key= os.getenv("UPSTAGE_API_KEY"),
        model="solar-embedding-1-large-passage"
    )
    
    return Chroma.from_documents(documents, embedding=embeddings)