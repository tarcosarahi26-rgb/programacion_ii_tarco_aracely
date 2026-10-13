"""
Control de flota de Naboo
"""

naves = [
    {
        "nombre": "Caza N-1",
        "combustible": 80,
        "droides": ["R2-D2", "R2-A6"]
    },
    {
        "nombre": "Caza Real",
        "combustible": 35,
        "droides": ["R2-N3"]
    },
    {
        "nombre": "Transporte",
        "combustible": 65,
        "droides": ["R2-D2", "R2-A6"]
    }
]

naves_listas = 0
naves_recargas = 0
total_droides = 0

for numero, nave in enumerate(naves, start=1):
    print("--- Nave : {numero}-{nave}")
    if nave["combustible"]>=50:
        print("Estado inical: LISTA")
        naves_listas+=1
    else:
        print("Estado inical: Recargar ")    
        naves_recarga+=1
        ciclo=0
        while nave["combustible"] <=50:
            ciclo+=1
            nave["combustible"]+=10
        total_ciclos+=ciclo
        print("Regarga completa")
        print("Estado Final: LISTA")    
    total_droides =len(nave["droides"])
    for droide in nave["droides"]:
        print(f"Droide: {droide}")


print("=================================================")
print("RESUMEN")
print("=================================================")
print(f"Total naves: {len(naves)}")
print(f"Naves listas inicialmente: {naves_listas}")
print(f"Naves recargadas: {naves_recargas}")
print(f"Total droides: {total_ciclos}")
print(f"Total ciclos: {total_droides}")