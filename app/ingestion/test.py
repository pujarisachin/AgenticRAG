
from app.ingestion.loaders import load_multiple_documents
from app.ingestion.cleaner import clean_documents

docs = load_multiple_documents("app/Data/raw")

cleaned_docs = clean_documents(docs)

print(cleaned_docs[0].page_content)
print(cleaned_docs[0].metadata)


