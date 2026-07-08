from fastapi import APIRouter
from ..repositories.verbo_repository import get_verbo

router = APIRouter()


@router.get("/")
def home():
    return {"message": "API funcionando!"}


@router.get("/assuntos/{assunto}")
def get_assuntos(assunto: str):
    banco_dados = {
        'verbo': get_verbo(),
        'substantivo': 'ainda não implementado',
        'adjetivo': 'ainda não implementado',
        'advérbio': 'ainda não implementado',
    }

    return banco_dados.get(assunto, {"message": "Assunto não encontrado."})



