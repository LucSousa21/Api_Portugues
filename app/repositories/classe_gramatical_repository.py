from ..core.supabase import supabase

# Função responsável por buscar todas as classes gramaticais no banco de dados.
def get_classe_gramatical():
    
    resposta = (
        supabase
        .table('classe_gramatical')
        .select('*')
        .execute()
    )

    return resposta.data