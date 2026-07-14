from pydantic import BaseModel

# Modelo responsável por definir e validar a estrutura dos dados dos modos verbais
class ModoVerbal(BaseModel):
    id: int | None = None
    nome: str
    definicao: str
    classe_id: int

# Modelo responsável por definir e validar a estrutura dos dados dos tempos verbais
class TempoVerbal(BaseModel):
    id: int | None = None
    nome: str
    definicao: str
    modo_id: int


