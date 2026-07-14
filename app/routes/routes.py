from fastapi import APIRouter
from ..services import (
    classes_gramaticais,
    verbo_formatado,
    substantivo_formatado,
    adjetivo_formatado,
    adverbio_formatado,
    artigo_formatado,
    pronome_formatado,
    numeral_formatado,
    preposicao_formatado,
    conjuncao_formatado,
    interjeicao_formatado,
)

router = APIRouter()

# Rotas para os metodos GET

@router.get("/")
def home():
    return {"message": "Bem Vindo!"}


@router.get("/assuntos")
def get_todas_classes():
    classes = classes_gramaticais()

    return classes


@router.get("/assuntos/{assunto}")
def get_assuntos(assunto: str):
    banco_dados = {
        'verbo': verbo_formatado(),
        'substantivo': substantivo_formatado(),
        'adjetivo': adjetivo_formatado(),
        'adverbio': adverbio_formatado(),
        'artigo': artigo_formatado(),
        'conjuncao': conjuncao_formatado(),
        'interjeicao': interjeicao_formatado(),
        'numeral': numeral_formatado(),
        'preposicao': preposicao_formatado(),
        'pronome': pronome_formatado(),

    }

    return banco_dados.get(assunto, {"message": "Assunto não encontrado."})




