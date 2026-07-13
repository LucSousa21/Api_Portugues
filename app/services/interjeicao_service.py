from ..repositories.classe_gramatical_repository import get_classe_gramatical

def interjeicao_formatado():
    dado = get_classe_gramatical()
    resposta = {
        'interjeicao': dado[9]
    }


    return resposta