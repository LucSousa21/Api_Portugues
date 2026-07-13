from ..repositories.classe_gramatical_repository import get_classe_gramatical

def substantivo_formatado():
    dado = get_classe_gramatical()
    resposta = {
        'substantivo': dado[1]
    }


    return resposta

