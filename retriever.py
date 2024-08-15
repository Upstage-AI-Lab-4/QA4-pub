class Retriever:
    def __init__(self, vector_store, embeddings):
        self.vector_store = vector_store
        self.embeddings = embeddings
    
    def retrieve(self, query, top_k=5):
    
        query_embedding = self.embeddings.embed_query(query)
        results = self.vector_store.similarity_search_by_vector(query_embedding, k=top_k)
        return results
