
from poo_Guerrero import Guerrero
class saiyajin(Guerrero):
    def __init__(self, nombre:str):
        super().__init__(nombre)
    def transformarse(self):
        print(self.nombre,"se transforma en super saiyajin" )

goku=saiyajin("goku")
goku.presentarse()
goku.transformarse()
