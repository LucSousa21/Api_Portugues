from ..repositories.classe_gramatical_repository import get_classe_gramatical

def artigo_formatado():
    dado = get_classe_gramatical()
    resposta = {
        'artigo': dado[3]
    }


    return resposta