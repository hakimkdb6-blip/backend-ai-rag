def moyenne( nombres: list[float])->float:
    return sum(nombres)/ len(nombres)

def saluer(nom: str, formel: bool = False) -> str:
    if formel:
        return f"Bonjour Monsieur/Madame {nom}"
    return f"Salut {nom} !"

def total (values :dict [str, int])-> int:
 return  sum(values.values())

print ( moyenne([10.0,12.5,15.0]))
print (saluer("Ali"))
print(saluer("Ali", formel=True))
print(total({"a": 1, "b": 2, "c": 3}))