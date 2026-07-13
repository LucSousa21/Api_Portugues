from ..repositories.classe_gramatical_repository import get_classe_gramatical

def preposicao_formatado():
    dado = get_classe_gramatical()
    resposta = {
        'preposicao': dado[7]
    }


    return resposta