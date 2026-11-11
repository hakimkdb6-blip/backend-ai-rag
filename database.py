import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

DATABASE_URL = os.environ["DATABASE_URL"]
engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    resultat = conn.execute(text("SELECT * FROM notes"))
    for ligne in resultat:
        print(ligne)