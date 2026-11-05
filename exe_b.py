import asyncio
import time
async def simuler_appel(nom: str, delai: float) -> str:
    await asyncio.sleep(delai)
    return f"{nom} terminé après {delai}s"

async def sequentiel() -> None:
    debut = time.perf_counter()
    for nom, delai in [("A", 1.0), ("B", 2.0), ("C", 1.5)]:
        print(await simuler_appel(nom, delai))
    print(f"Séquentiel : {time.perf_counter() - debut:.2f}s\n")

async def parallele() -> None:
    debut = time.perf_counter()
    resultats = await asyncio.gather(
        simuler_appel("A", 1.0),
        simuler_appel("B", 2.0),
        simuler_appel("C", 1.5),
    )
    for r in resultats:
        print(r)
    print (f"Parallèle : {time.perf_counter() - debut:.2f}s"
           )
async def main() -> None:
    await sequentiel()
    await parallele()

asyncio.run(main())