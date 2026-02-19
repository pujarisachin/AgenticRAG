from typing import List
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from app.core.logging import get_logger
from app.core.config import get_settings

logger = get_logger(__name__)


def chunk_document(documents:List[Document]):
    """Split documents into Semantically meaningfull documents"""
    settings = get_settings()
    chunk_size = getattr(settings,"default_chunk_size",800)
    chunk_overlap = getattr(settings,"default_chunk_overlap",150)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size = chunk_size,
        chunk_overlap = chunk_overlap
    )


    logger.info("splliting is started" f"Chunking len{documents}")

    chunks = splitter.split_documents(documents)

    return chunks
