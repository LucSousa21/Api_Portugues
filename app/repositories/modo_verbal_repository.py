from ..core.supabase import supabase

def get_modo_verbal():
    resposta = (
        supabase
        .table('modo_verbal')
        .select('*')
        .execute()
    )

    return resposta.data