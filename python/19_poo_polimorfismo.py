class Guerrero:
    nombre: str
    def __init__(self, nombre:str, poder_inicial: int, horas:int):
        self.nombre = nombre
        self.poder_inicial = poder_inicial
        self.horas = horas


    def atacar(self):
        print(f"{self.nombre}realiza un  ataque")


    def calcula_poder(self):
        return self.poder_inicial
          
class Goku(Guerrero):
    def __init__(self, nombre: str, poder_inicial: int, horas:int):
        super().__init__(nombre, poder_inicial, horas)


    def atacar(self):
        print(self.nombre, "utiliza el kamehameha")

    def calcula_poder(self):
        return self.poder_inicial + self.horas*100

    
class Vegeta(Guerrero):
    def __init__(self, nombre:str, poder_inicial:int, horas:int):
        super().__init__(nombre, poder_inicial, horas)

    def atacar(self):
            print(self.nombre, "utiliza final flash")


    def calcula_poder(self):
             return self.poder_inicial + self.horas*150       

Goku= Goku("grand goku", 150, 50)
Vegeta= Vegeta("vegeta", 200, 80)
Goku.atacar()
Vegeta.atacar()
print(Goku.calcula_poder())
print(Vegeta.calcula_poder())


        

