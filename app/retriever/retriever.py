from typing import List,Optional
from app.core.logging import get_logger
from langchain_core.documents import Document

logger = get_logger(__name__)

class Retriever():
    def __init__(self,vectorstore):
        self.vector_store = vectorstore

    def similarity_search(
            self,
            query:str,
            k :int = 5):
        logger.info(f"simmilarity search | k = {k}")
        return self.vector_store.similarity_search(query, k=k)
    
    def mmr_search(
            self,
            query:str,
            k :int = 5,
            fetch_k = 20,
            lambda_mult: float = 0.5
    ):
        logger.info(f"mmr search k|{k} and lambda= {lambda_mult}")
        return self.vector_store.max_marginal_relevance_search(
            query = query,
            k=k,
            fetch_k=fetch_k,
            lambda_mult=lambda_mult
        )
