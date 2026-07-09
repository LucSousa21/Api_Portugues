from pydantic import BaseModel

class ClasseGramatical(BaseModel):
    id: int | None = None
    nome: str
    definicao: str