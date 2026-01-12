
from app.ingestion.loaders import load_multiple_documents
from app.ingestion.cleaner import clean_documents
from app.ingestion.chunking import chunk_document

docs = load_multiple_documents("app/Data/raw")
cleaned_docs = clean_documents(docs)
chunks = chunk_document(cleaned_docs)

print(f"Documents: {len(cleaned_docs)}")
print(f"Chunks: {len(chunks)}")
print(chunks[0].page_content)
print(chunks[0].metadata)

