from fastapi import FastAPI

app = FastAPI()

aluno = {
    "matricula": "2024118ISINF0029",
    "nome": "ANA CLARA DOS SANTOS"
}

@app.get("/")
def inicio():
    return aluno
