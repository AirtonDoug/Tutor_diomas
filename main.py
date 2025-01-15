from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_db_and_tables
from routes import alunos, turmas, tutores


# Configurações de inicialização
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

# Inicializa o aplicativo FastAPI
app = FastAPI(lifespan=lifespan)

# Rotas para Endpoints
app.include_router(alunos.router)
app.include_router(turmas.router)
app.include_router(tutores.router)