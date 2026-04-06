from app.repositories.analisador_repository import AnalisadorRepository

class AnalisadorService:
    def __init__(self, repo: AnalisadorRepository):
        self.repo = repo 

    def obter_relatorio_usuario(self, user_id: int):
        return self.repo.calcular_estatísticas(user_id)
