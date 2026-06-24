from fastapi import APIRouter
from app.data import assuntos

router = APIRouter()


@router.get("/")
def home():
    return {"message": "API funcionando!"}


@router.get("/assuntos/{assunto}")
def get_assuntos(assunto: str):
    return assuntos.get(assunto)

