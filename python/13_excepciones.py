


print("=======CONTROL DE EBERGIA=====")
energia_texto= "ochenta"
try:
    energia = int(energia_texto)
    print(energia)
except ValueError:
    print("Error: debe ser numerico")


print("Fin del sistema")    


"""
ValueError
TYpeError
KeyError
IndexError
ZeroDivisionError
"""


def calcular_energia(total, cantidad):
    try:
        resultado = total/cantidad
    except ZeroDivisionError:
        print("Error: divisiones entre  cero")
        return None

    except TypeError:
        print("Error: valores deben ser numericos")



print("Caso1:", calcular_energia(100,4))        
print("Caso2:", calcular_energia(100,0))        
print("Caso3:", calcular_energia(100,"cuatro"))  




print("======DIAGNOSTICO R2-D2==============")
try:
    energia = int("cuatro")
    print("energia", energia)
except ValueError:
     print("Error de lectura")
else:
    print("diagnostico completado")
finally:
    print("Cerrando diagnostico")



def validar_energia(energia):
    if type(energia) is not int:
        raise TypeError("La enrgia dbe ser numero entero")
    if energia<0 or energia>100:
        raise ValueError("la energia dbe estar entre 0 y 100")
    return energia


try:
    resultado = validar_energia(60)
    print("Energia", resultado)
except(TypeError,ValueError) as error:
    print("Error: ", error)