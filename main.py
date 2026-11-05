from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/saluer/{nom}")
def saluer(nom: str):
    return {"message": f"Salut {nom} !"}