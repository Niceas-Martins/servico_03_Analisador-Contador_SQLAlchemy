import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controllers import analisador_controller

app = FastAPI(title = "Serviço 3 - Analisador de Estatísticas")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analisador_controller.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8003)