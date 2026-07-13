from pydantic import BaseModel

class Exemplo(BaseModel):
    id: int | None = None
    frase: str
    classe_id: int