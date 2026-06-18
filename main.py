from fastapi import FastAPI

app = FastAPI()

aluno = {
    "matricula": "2024118ISINF0027",
    "nome": "KAIO FELLIPE BARBOSA DANTAS"
}

@app.get("/")
def inicio():
    return aluno
