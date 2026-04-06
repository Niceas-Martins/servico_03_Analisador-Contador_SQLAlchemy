from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.repositories.analisador_repository import AnalisadorRepository  
from app.services.analisador_service import AnalisadorService 

router = APIRouter(prefix="/api")

@router.get("/estatisticas/{user_id}")
def read_stats(user_id: int, db: Session = Depends(get_db)):
    repo = AnalisadorRepository(db)
    service = AnalisadorService(repo)
    return service.obter_relatorio_usuario(user_id)
