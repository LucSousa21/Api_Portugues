from ..core.supabase import supabase

def get_exemplo_verbal():
    
    resposta = (
        supabase
        .table('exemplo_verbal')
        .select('*')
        .execute()
    )

    return resposta.data