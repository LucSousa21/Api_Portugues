from pydantic import BaseSettings, SetingsConfigDict
from os import getenv

class Settings(BaseSettings):
    supabase_url: str
    supabase_key: str
    supabase_token: str

    model_config = SetingsConfigDict(env_file=".env")

settings = Settings()