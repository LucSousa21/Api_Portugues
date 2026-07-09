from ..repositories.modo_verbal_repository import get_modo_verbal
from ..repositories.tempo_verbal_repository import get_tempo_verbal
from ..repositories.exemplo_repository import get_exemplo_verbal
from ..repositories.classe_gramatical_repository import get_classe_gramatical

def exemplo_formatado():    
    exemplo_verbal = get_exemplo_verbal()
    exemplos = {}
    for linha in exemplo_verbal:
        tempo_id = linha["tempo_id"]
        frase = linha["frase"]
        exemplos.setdefault(tempo_id, []).append((frase))
    
    return exemplos



def tempo_verbal_formatado():

    tempo_verbal =  get_tempo_verbal()

    tempo_formatado = {}
    for linha in tempo_verbal:

        tempo_id = linha['id']
        nome = linha['nome']
        modo_id = linha['modo_id']
        exemplo = exemplo_formatado()
        tempo_formatado.setdefault(modo_id, []).append(({
            'nome': nome, 
            'exemplo': exemplo.get(tempo_id, [])
        }))
    
    return tempo_formatado



def modo_verbal_formatado():
    modo_verbal = get_modo_verbal()

    modo_formatado = []
    for linha in modo_verbal:

        modo_id = linha['id']
        nome = linha['nome']
        classe_id = linha['classe_id']
        tempo_formatado = tempo_verbal_formatado()
        modo_formatado.append({
            'modo_id': modo_id,
            'nome': nome,
            'classe_id': classe_id,
            'tempos': tempo_formatado.get(modo_id, [])
        })

    return modo_formatado





def verbo_formatado():
    definicao = get_classe_gramatical()
    resultado = {
        'verbo': definicao[0],
        'modos': modo_verbal_formatado()


    }

    return resultado


