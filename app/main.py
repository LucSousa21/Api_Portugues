from fastapi import FastAPI
from .routes import router

# Inicializa a aplicação FastAPI e registra as rotas da API.
app = FastAPI()
app.include_router(router)