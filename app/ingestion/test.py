
from app.ingestion.loaders import load_multiple_documents
from app.ingestion.cleaner import clean_documents
from app.ingestion.chunking import chunk_document
from app.ingestion.metadata import enrich_metadata
from app.vectorstore.embeddings import get_embedding_model

docs = load_multiple_documents("app/Data/raw")
model = get_embedding_model()


cleaned_docs = clean_documents(docs)
print(cleaned_docs)
chunks = chunk_document(cleaned_docs)
enriched_chunks = enrich_metadata(chunks)

texts = [doc.page_content for doc in enriched_chunks]
vec = model.embed_documents(texts)

print(f"Documents: {len(vec)}")
print(f"Chunks: {len(vec)}")

for v in vec:
    print(v)
    

