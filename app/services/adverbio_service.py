from ..repositories.classe_gramatical_repository import get_classe_gramatical

def adverbio_formatado():
    dado = get_classe_gramatical()
    resposta = {
        'adverbio': dado[6]
    }


    return resposta