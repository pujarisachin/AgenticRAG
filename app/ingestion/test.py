
from app.ingestion.loaders import load_multiple_documents

docs = load_multiple_documents("app/Data/raw")

print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata)
