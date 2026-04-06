from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Tarefa(Base):
    __tablename__ = 'Tarefa'

    id = Column(Integer, primary_key = True)
    titulo = Column(String)
    concluida = Column(Boolean, default=False)
    usuarioId = Column(Integer)
    