import asyncio
import json

async def simuler_llm(question: str) -> dict[str, str]:
    await asyncio.sleep(1)  # simule le temps de réponse d'un LLM
    return {"question": question, "reponse": f"Réponse simulée à : {question}"}

async def main() -> None:
    questions: list[str] = [
        "Qu'est-ce qu'un token ?",
        "Qu'est-ce qu'un RAG ?",
        "Pourquoi utiliser un cache ?",
    ]
    resultats = await asyncio.gather(*(simuler_llm(q) for q in questions))
    print(json.dumps(resultats, indent=2, ensure_ascii=False))

asyncio.run(main())