
from app.ingestion.loaders import load_multiple_documents
from app.ingestion.cleaner import clean_documents
from app.ingestion.chunking import chunk_document
from app.ingestion.metadata import enrich_metadata
from app.vectorstore.embeddings import get_embedding_model
from app.vectorstore.store import build_vector_store
from app.retriever.retriever import Retriever

docs = load_multiple_documents("app/Data/raw")
model = get_embedding_model()


cleaned_docs = clean_documents(docs)
print(cleaned_docs)
chunks = chunk_document(cleaned_docs)
enriched_chunks = enrich_metadata(chunks)

store = build_vector_store(enriched_chunks)

retriever = Retriever(store)


print("===**********************************************************************Similarity Search ===")
results = retriever.similarity_search(
    "What is this document about?", k=3
)

for r in results:
    print(r.metadata["chunk_id"])

print("\n=== ###############################################################3333MMR Search ===")
results = retriever.mmr_search(
    "What is this document about?", k=3
)

for r in results:
    print(r.metadata["chunk_id"])

#result = store.similarity_search("Inventive",k=5)

# texts = [doc.page_content for doc in enriched_chunks]
# vec = model.embed_documents(texts)


# print(f"Documents: {len(vec)}")
# print(f"Chunks: {len(vec)}")

# for v in vec:
#     print(v)

# for r in result:
#     print("*************************************")
#     print(r.page_content)
#     print("########")
#     print(r.metadata)
    

