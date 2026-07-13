from ..repositories.classe_gramatical_repository import get_classe_gramatical

def pronome_formatado():
    dado = get_classe_gramatical()
    resposta = {
        'pronome': dado[4]
    }


    return resposta