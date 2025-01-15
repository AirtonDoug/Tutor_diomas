from fastapi import APIRouter, HTTPException, Depends, Query
from sqlmodel import Session, select
from sqlalchemy.orm import joinedload
from models.turmas import Turma, TurmaAluno, TurmaWithAlunos , TurmaWithAlunosTutor , TurmaWithTutor
from models.alunos import alunos
from models.turores import tutores
from database import get_session
from datetime import datetime

router = APIRouter(
    prefix="/turmas",  # Prefixo para todas as rotas
    tags=["Turmas"],   # Tag para documentação automática
)

# Turmas
@router.post("/", response_model=Turma)
def create_turma(turma: Turma, session: Session = Depends(get_session)):
    session.add(turma)
    session.commit()
    session.refresh(turma)
    return turma

@router.get("/", response_model=list[TurmaWithAlunosTutor])
def read_turmas(offset: int = 0, limit: int = Query(default=10, le=100), 
                session: Session = Depends(get_session)):
    statement = (select(Turma).offset(offset).limit(limit).options(joinedload(Turma.alunos),joinedload(Turma.tutores)))
    return session.exec(statement).all()