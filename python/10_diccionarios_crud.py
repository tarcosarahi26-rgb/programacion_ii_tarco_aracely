droides = [
    {
        "codigo": "B1-001",
        "modelo": "B1",
        "energia": 90,
        "activo": True
    },
    {
        "codigo": "B1-002",
        "modelo": "B1",
        "energia": 40,
        "activo": False
    },
    {

        "codigo": "DRO-001",
        "modelo": "droideka",
        "energia": 80,
        "activo": True
    }
]
cantidad_droides = len(droides)
print(cantidad_droides)
print(droides)
nuevo_droide= {
        "codigo": "B1-004",
        "modelo": "B1",
        "energia": 100,
        "activo": True

}
#CRUD
#CREATE
droides.append(nuevo_droide)
print(len(droides))
print(droides)
#READ
droide = droides [0]
print(f"codigo : {droide["codigo"]}")
print(f"codigo : {droide["codigo"]}")
print(f"codigo : {droide["codigo"]}")
print(f"codigo : {droide["codigo"]}")
print(f"codigo : {droide["codigo"]}")
#UPDATE
droide = droides[2]
droide["codigo"]="DR0-002"
droide["energia"]=85
droide["activo"]=False
print(f"droides : {droides}")
#DELETE
eliminado =droides.pop(2)
print(f"droides : {droides}")


