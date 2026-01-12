
from app.ingestion.loaders import load_multiple_documents
from app.ingestion.cleaner import clean_documents
from app.ingestion.chunking import chunk_document
from app.ingestion.metadata import enrich_metadata

docs = load_multiple_documents("app/Data/raw")


cleaned_docs = clean_documents(docs)
print(cleaned_docs)
chunks = chunk_document(cleaned_docs)
enriched_chunks = enrich_metadata(chunks)

print(f"Documents: {len(enriched_chunks)}")
print(f"Chunks: {len(enriched_chunks)}")

for chunk in enriched_chunks:
    print(chunk.page_content)
    print(chunk.metadata)

