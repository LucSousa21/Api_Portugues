from ..core.supabase import supabase

def get_classe_gramatical():
    
    resposta = (
        supabase
        .table('classe_gramatical')
        .select('*')
        .execute()
    )

    return resposta.data