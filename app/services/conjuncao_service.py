from ..repositories.classe_gramatical_repository import get_classe_gramatical

def conjuncao_formatado():
    dado = get_classe_gramatical()
    resposta = {
        'conjuncao': dado[8]
    }


    return resposta