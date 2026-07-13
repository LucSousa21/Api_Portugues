from ..repositories.classe_gramatical_repository import get_classe_gramatical

def classes_gramaticais():
    dado = get_classe_gramatical()
    resposta = {
        'Classes Gramaticais': dado
    }


    return resposta