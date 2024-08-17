
class Retriever:
    def __init__(self, vector_store):
        self.vector_store = vector_store
        # self.embeddings = embeddings
    
    # def retrieve2(self, query, top_k=5):
    
    #     query_embedding = self.embeddings.embed_query(query)
    #     results = self.vector_store.similarity_search_by_vector(query_embedding, k=top_k)
    #     return results

    def retrieve(self):
    
        retriever = self.vector_store.as_retriever(
        # 검색 유형을 "유사도 점수 임계값"으로 설정합니다.
        # search_type="similarity_score_threshold",
        # 검색 인자로 점수 임계값을 0.5로 지정합니다.
        search_kwargs={
            # "score_threshold": 0.5 , 
            "k":2},
        )
        
        return retriever