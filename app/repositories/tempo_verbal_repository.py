from ..core.supabase import supabase

def get_tempo_verbal():
    resposta = (
        supabase
        .table('tempo_verbal')
        .select('*')
        .execute()

    )

    return resposta.data