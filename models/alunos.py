from sqlmodel import SQLModel , Field

class Aluno(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str 
    email: str
    login: str
    senha: str
    nivel: str
    aulas_assistidas: int
    turma_id: int | None = Field(default=None, foreign_key="turma.id")