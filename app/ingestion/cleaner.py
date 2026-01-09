import re
from typing import List
from app.core.logging import get_logger
from langchain_core.documents import Document


logger = get_logger(__name__)


def clean_text(text:str):
    if not text:
        return ""
    
    #removes null bytes
    text = text.replace("\x00","")

    #normalize white space
    text = re.sub(r"\s+", " ", text)

     # Remove non-printable characters
    text = "".join(ch for ch in text if ch.isprintable())

    return text.strip()

def clean_documents(Documents:List[Document]):
    cleaned_final_docs: List[Document] = []

    for doc in Documents:
        cleaned_content = clean_text(doc.page_content)

        cleaned_doc = Document(
            page_content=cleaned_content,
            metadata = doc.metadata.copy()
        )

        cleaned_final_docs.append(cleaned_doc)

        return cleaned_final_docs