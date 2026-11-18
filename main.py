from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import text

from database import engine

app = FastAPI()


class Note(BaseModel):
    titre: str = Field(min_length=1)
    contenu: str | None = None


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/notes")
def creer_note(note: Note):
    # begin() ouvre une transaction et la valide (commit) à la sortie du bloc.
    with engine.begin() as conn:
        resultat = conn.execute(
            text(
                "INSERT INTO notes (titre, contenu) "
                "VALUES (:titre, :contenu) "
                "RETURNING id, titre, contenu"
            ),
            {"titre": note.titre, "contenu": note.contenu},
        )
        ligne = resultat.mappings().first()
    return dict(ligne)


@app.get("/notes")
def lister_notes():
    with engine.connect() as conn:
        resultat = conn.execute(
            text("SELECT id, titre, contenu FROM notes ORDER BY id")
        )
        lignes = resultat.mappings().all()
    return [dict(ligne) for ligne in lignes]


@app.get("/notes/{note_id}")
def lire_note(note_id: int):
    with engine.connect() as conn:
        resultat = conn.execute(
            text("SELECT id, titre, contenu FROM notes WHERE id = :id"),
            {"id": note_id},
        )
        ligne = resultat.mappings().first()
    if ligne is None:
        raise HTTPException(status_code=404, detail="Note introuvable")
    return dict(ligne)
