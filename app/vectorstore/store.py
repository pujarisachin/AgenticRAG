from langchain_community.vectorstores import FAISS
from app.core.logging import get_logger
from app.vectorstore.embeddings import get_embedding_model
from app.core.config import get_settings

logger = get_logger(__name__)

def build_vector_store(documents):
    embeddings = get_embedding_model()

    vector_store = FAISS.from_documents(
        embedding=embeddings,
        documents=documents
    )

    return vector_store

