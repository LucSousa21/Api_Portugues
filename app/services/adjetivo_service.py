from ..repositories.classe_gramatical_repository import get_classe_gramatical

def adjetivo_formatado():
    dado = get_classe_gramatical()
    resposta = {
        'adjetivo': dado[2]
    }


    return resposta