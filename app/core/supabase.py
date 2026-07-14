from supabase import create_client
from .config import settings

# Cria a instância do cliente para comunicação com o Supabase.
supabase = create_client(
    settings.supabase_url,
    settings.supabase_key
    )