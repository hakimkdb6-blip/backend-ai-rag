from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Question(BaseModel):
    texte: str = Field(min_length=3)
    langue: str = "fr"

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/saluer/{nom}")
def saluer(nom: str):
    return {"message": f"Salut {nom} !"}

@app.post("/question")
def poser_question(q: Question):
    return {"reponse": f"Tu as demandé : {q.texte}", "langue": q.langue}