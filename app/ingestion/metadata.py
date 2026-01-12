from typing import List
import hashlib
from langchain_core.documents import Document
from app.core.logging import get_logger

logger = get_logger(__name__)


def generate_doc_id(source_file:str):
    return hashlib.md5(source_file.encode()).hexdigest()

def enrich_metadata(chunks:List[Document]):
    """Adds document and chunk level metadata"""
    logger.info(f"enriching metadata for {len(chunks)}")
    enriched_chunks:List[Document] = []
    doc_counters={}

    for chunk in chunks:
        source = chunk.metadata.get("source_file","unknown")
        doc_id = generate_doc_id(source)

        if doc_id not in doc_counters:
            doc_counters[doc_id] = 0
        doc_counters[doc_id] +=1

        chunk_index = doc_counters[doc_id]

        enrich_metadata = chunk.metadata.copy()
        enrich_metadata["doc_id"] = doc_id
        enrich_metadata["chunk_id"] = f"{doc_id}_chunk_{chunk_index}"
        enrich_metadata["chunk_index"] = chunk_index

        enriched_chunk = Document(
            page_content=chunk.page_content,
            metadata = enrich_metadata
        )

        enriched_chunks.append(enriched_chunk)
    
    return enriched_chunks
