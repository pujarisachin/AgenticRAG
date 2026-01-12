import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from functools import lru_cache

ENV_NAME = os.getenv("APP_ENV","development")

load_dotenv(F".env.{ENV_NAME}")

class Settings(BaseSettings):
    app_name:str
    log_level:str
    openai_api_key:str
    vector_store_type:str
    default_chunk_size:int
    default_chunk_overlap : int

@lru_cache
def get_settings():
    return Settings()