# ciclo for

naves=[
    "Caza N-1", 
    "Nave real de Naboo", 
    "Transporte", 
] 
for nave in naves:
    print("Inspeccionando" , nave)

    print("inspección realizada")


    ronda = range(1,6)
    print("Tipo de dato en rondas:", type(ronda))
    for ronda in ronda:
        print(f"Ronda de vigilancia: {ronda}")
        print(f"Tipo de dato ronda: {type(ronda)}")


    droides= range(1,17,2)
    print("Tipo de dato en droides:", type(droides))
    for droide in droides:
        print(f"Reparar : droid B1-{droide}")
        print(f"Tipo de dato droid: {type(droide)}")


        planetas = ["Naboo", "Tatooine", "Coruscant"]

        recorrido = enumerate(planetas, start=5)
        for posicion, planeta in recorrido:
            print(f"Destino {posicion}: {planeta}")
            print(f"Tipo de datos: {type(posicion)}: {type(planeta)}")


            paises = ["Ecuador","Venezuela", "Chile", "Colombia", "Brasil", "Estados Unidos"]

            for pais in paises:
                if pais == "Chile":
                    continue
                if pais =="Brasil":
                    break
                print(f"Pais visitado: {pais}")


            jedi ={}
            jedi_activo={
                "nombre": "Obiwan",
                "fuerza":"120",
                "estilo_pelea":"Samurai",
                "misiones":["guerra alderan", "secuestro palpatine","escolta de leila"],
                "descripcion": {"estatura":1.80,
                                 "especie": "humana"} 
            }


            print(jedi_activo)

            nave=dict(nombre="AZ-1",capacidad=8, turbo_laser=2)
            print(nave)

            jedi["nombre"]= "Luck"
            jedi["fuerza"]= 150
            print(jedi)

            for clave, valor in jedi_activo.items():
                print(f" {clave} -  {valor}")