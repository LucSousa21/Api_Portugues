from pydantic import BaseModel

# Modelo responsável por definir e validar a estrutura dos dados
# das classes gramaticais
class ClasseGramatical(BaseModel):
    id: int | None = None
    nome: str
    definicao: str