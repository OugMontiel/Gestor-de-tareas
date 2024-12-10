import json

def Carga():
    with open("Base.json", "r", encoding='utf-8') as f:
        base = json.load(f)
    return base

def Guarda(diccionario):
    with open("Base.json", "w", encoding='utf-8') as f:
        json.dump(diccionario, f)
