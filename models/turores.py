from sqlmodel import Field, SQLModel

class TutorBase(SQLModel, table=True):
    id: int
    nome: str
    email: str
    login: str
    senha: str
    nivel: str
    lingua: str
    turma_responsavel: str
    turma_id: int = Field(default=None, foreign_key="turma.id")