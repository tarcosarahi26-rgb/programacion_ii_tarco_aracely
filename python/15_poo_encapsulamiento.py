class Guerrero:
    nombre: str 
    _poder: int

    def __init__(self, nombre: str, poder: int):
        self.nombre = nombre
        self.__poder = poder


    def get_poder(self):
        return self.__poder


vegeta=Guerrero("vegeta", 8000)
print("Guerrero: ", vegeta.nombre)
print("poder : ", vegeta.get_poder()) 


class CuentaZeni:
    titular: str
    __saldo: int

    def __init__(self, titular: str, saldo: int):
        self.titular = titular
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo


    def retirar_dinero(self, cantidad: int):
        if cantidad >0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print("Retiro realizado", cantidad)
        else:
            print("Retiro no permitido")


cuenta = CuentaZeni("Mr. Satan", 5000)
print("Titular: ", cuenta.titular)
print("saldo inicial", cuenta.get_saldo())
cuenta.retirar_dinero(500)
print("saldo final", cuenta.get_saldo())



class AlmacenSemillas:
    __cantidad: int

    def __init__(self, cantidad):
        self.__cantidad = cantidad

    def get_cantidad(self):
        return self.__cantidad
    
    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self.__cantidad = cantidad
        else:
            print("La cantidad no puede ser negativa.")

    def entrega_semillas(self, cantidad):
        if cantidad <= self.__cantidad:
            self.__cantidad = self.__cantidad - cantidad

            print(f"Entrega realizada correctamente {cantidad} semillas. ")
        else:
            print("No hay suficientes semillas para entregar.")

almacen = AlmacenSemillas(10)

print("Entrega Goku:")
almacen.entrega_semillas(3)

print("Entrega Yajirobe:")
almacen.entrega_semillas(9)

print("Cantidad de semillas disponibles:", almacen.get_cantidad())