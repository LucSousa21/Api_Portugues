from ..core.supabase import supabase

# Função responsável por buscar todos os tempos verbais no banco de dados
def get_tempo_verbal():
    resposta = (
        supabase
        .table('tempo_verbal')
        .select('*')
        .execute()

    )

    return resposta.data