from ..repositories.classe_gramatical_repository import get_classe_gramatical

def numeral_formatado():
    dado = get_classe_gramatical()
    resposta = {
        'numeral': dado[5]
    }


    return resposta