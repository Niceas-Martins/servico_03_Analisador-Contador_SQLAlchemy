from sqlalchemy.orm import Session
from models import Tarefa

class AnalisadorRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def calcular_estatísticas(self, user_id: int):
        total = self.db.query(Tarefa).filter(Tarefa.usuarioId == user_id).count()
        
        concluidas  = self.db.query(Tarefa).filter(
             Tarefa.usuarioId == user_id,
             Tarefa.concluida == True
        ).count()

        return{
            "usuarioId": user_id,
            "total": total,
            "concluidas": concluidas,
            "pendentes": total - concluidas
        }