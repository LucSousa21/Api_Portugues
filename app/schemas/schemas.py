from pydantic import BaseModel


class Verbo(BaseModel):
    id: int
    definicao: str


class ModoVerbal(BaseModel):
    id: int | None = None
    nome: str
    definicao: str
    verbo_id: int

class TempoVerbal(BaseModel):
    id: int | None = None
    nome: str
    definicao: str
    modo_id: int


class ExemplosVerbo(BaseModel):
    id: int | None = None
    frase: str
    tempo_id: int