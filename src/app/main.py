# Bibiotecas Padrões

# Bibliotecas de Terceiros
from fastapi import FastAPI

# Imports locais

# instância principal do app
app = FastAPI(
    title="Cardápio Online",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# app.include_router(groups.router, prefix="/api/v1/groups", tags=["groups"])
# app.include_router(products.router, prefix="/api/v1/products", tags=["products"])

@app.get("/ping", tags=["health"])
async def ping():
    return {"message": "pong"}