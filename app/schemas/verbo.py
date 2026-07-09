from pydantic import BaseModel

class ModoVerbal(BaseModel):
    id: int | None = None
    nome: str
    definicao: str
    classe_id: int

class TempoVerbal(BaseModel):
    id: int | None = None
    nome: str
    definicao: str
    modo_id: int


