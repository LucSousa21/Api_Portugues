from ..core.supabase import supabase

# Função responsável por buscar todos os modos verbais no banco de dados
def get_modo_verbal():
    resposta = (
        supabase
        .table('modo_verbal')
        .select('*')
        .execute()
    )

    return resposta.data