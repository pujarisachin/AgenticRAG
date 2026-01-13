from langchain_openai import OpenAIEmbeddings
from app.core.config import get_settings
from app.core.logging import get_logger


logger = get_logger(__name__)

def get_embedding_model():
    settings = get_settings()

    return OpenAIEmbeddings(
        openai_api_key = settings.openai_api_key,
        model = "text-embedding-3-small"
    )