from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

class Question(BaseModel):
    texte: str = Field(min_length=3)
    langue: str = "fr"

class Note(BaseModel):
    
    titre: str = Field(min_length=1)
    contenu: str

notes: list[dict] = []

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/saluer/{nom}")
def saluer(nom: str):
    return {"message": f"Salut {nom} !"}

@app.post("/question")
def poser_question(q: Question):
    return {"reponse": f"Tu as demandé : {q.texte}", "langue": q.langue}

@app.post("/notes")
def creer_note(note: Note):
    nouvelle = {"id": len(notes) + 1, "titre": note.titre, "contenu": note.contenu}
    notes.append(nouvelle)
    return nouvelle

@app.get("/notes")
def lister_notes():
    return notes

@app.get("/notes/{note_id}")
def lire_note(note_id: int):
    for n in notes:
        if n["id"] == note_id:
            return n
    raise HTTPException(status_code=404, detail="Note introuvable")