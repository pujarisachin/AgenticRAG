from pathlib import Path
from typing import List
from langchain_core.documents import Document
from langchain_community.document_loaders import (PyPDFLoader,Docx2txtLoader,TextLoader)
from app.core.logging import get_logger

logger = get_logger(__name__)

Supported_extentions = {".pdf",".docx",".txt"}

def Load_single_file(filepath:Path):
    suffix = filepath.suffix.lower()
    if suffix == ".pdf":
        loader = PyPDFLoader(str(filepath))
    elif suffix == ".docx":
        loader = Docx2txtLoader(str(filepath))
    elif suffix == ".txt":
        loader = TextLoader(str(filepath),encoding="utf-8")
    else:
        raise ValueError("File Format is not supported")
    
    document = loader.load()

    for doc in document:
        doc.metadata["Source File"] = filepath.name
    
    return document

def load_multiple_documents(directoryPath:Path):
    directoryPath = Path(directoryPath)

    if not directoryPath.exists():
        raise FileNotFoundError("Path does not exist: {directoryPath}")
    
    all_documents:list[Document] = []

    if directoryPath.is_file():
        doc = Load_single_file(directoryPath)
        all_documents.extend(doc)

    # list all files from directory

    files = [
        f for f in directoryPath.iterdir()
        if f.is_file() and f.suffix.lower()  in Supported_extentions
    ]

    if not files:
        logger.info("no supported files in directory")
    
    for file in files:
        doc = Load_single_file(file)
        all_documents.extend(doc)

    return all_documents