from langchain_upstage import UpstageEmbeddings
from langchain_chroma import Chroma

def create_vector_store(documents):
    embeddings = UpstageEmbeddings(
        api_key="your_api_key_here",
        model="solar-embedding-1-large-passage"
    )
    
    return Chroma.from_documents(documents, embedding=embeddings)