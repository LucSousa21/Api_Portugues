from pydantic import BaseModel

# Modelo responsável por definir e validar a estrutura dos dados dos exemplos
class Exemplo(BaseModel):
    id: int | None = None
    frase: str
    classe_id: int