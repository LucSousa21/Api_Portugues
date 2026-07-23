from fastapi import FastAPI
from .routes import router

# Inicializa a aplicação FastAPI e registra as rotas da API.
app = FastAPI(
    title="API Português",
    description="API para consultar assuntos de Portguês",
    version="1.0.0"
)
app.include_router(router)