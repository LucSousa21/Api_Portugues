from ..core.supabase import supabase

# Função responsável por buscar todos os exemplos verbais no banco de dados
def get_exemplo_verbal():
    
    resposta = (
        supabase
        .table('exemplo_verbal')
        .select('*')
        .execute()
    )

    return resposta.data