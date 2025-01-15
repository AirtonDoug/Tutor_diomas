from sqlmodel import Field, SQLModel
from sqlmodel import Relationship
from .alunos import Aluno
from .turores import Tutor


class TurmaAluno(SQLModel,table=True):
    turma_id: int = Field(default=None, primary_key=True)
    aluno_id: int = Field(default=None, primary_key=True)

class TurmaBase(SQLModel, table=True):
    id: int
    nome: str
    tutor_responsavel: str
    alunos_participantes: str
    aulas: int
    nivel: str
    lingua: str
    horario: str
    dia: str
    sala: str
    link: str
    status: str
    observacoes: str
    tutor_id: int = Field(default=None, foreign_key="tutor.id")

class Turma(TurmaBase,table = True):
    id: int = Field(default=None, primary_key=True)
    alunos: list["Aluno"] = Relationship(back_populates="turma")
    tutor: "Tutor" = Relationship(back_populates="turma")
    
class TurmaWithAlunosTutor(TurmaBase):
    alunos: list[Aluno]
    tutor: Tutor
class TurmaWithAlunos(TurmaBase):
    alunos: list[Aluno]
class TurmaWithTutor(TurmaBase):
    tutor: Tutor