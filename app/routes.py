from fastapi import APIRouter
from app.schemas import Usuario
from app.data import assuntos

router = APIRouter()

usuarios = []

@router.get("/")
def home():
    return {"message": "API funcionando!"}


