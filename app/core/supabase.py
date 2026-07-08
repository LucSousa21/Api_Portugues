from supabase import create_client
from os import getenv
from dotenv import load_dotenv
load_dotenv()
SUPABASE_URL = getenv("SUPABASE_URL")
SUPABASE_KEY = getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)