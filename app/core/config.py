from pydantic_settings import BaseSettings, SettingsConfigDict
from os import getenv

class Settings(BaseSettings):
    supabase_url: str
    supabase_key: str
    supabase_token: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()