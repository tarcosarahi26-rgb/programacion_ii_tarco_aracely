# Condicional if
# simple


combustible = 5
if combustible >= 10:
    print("puedes despegar")


# condicional if-else
creditos = int(input("Ingrese la cantidad de creditos: "))
precio_repuestos =int(input("Ingrese el precio de los repuestos: "))
if creditos >= precio_repuestos:
    print("puedes comprar los repuestos")
else:
    print("no tienes suficientes creditos para comprar los repuestos")

# if anidado
if creditos >= precio_repuestos:
    print("puedes comprar los repuestos")
    if creditos > precio_repuestos:
        print("te sobran creditos")
    else:
        print("no te sobran creditos")
else:
    print("no tienes suficientes creditos para comprar los repuestos")

# condicional if-elif-else
if creditos > precio_repuestos:
    print("puedes comprar los repuestos y te sobran creditos")
elif creditos == precio_repuestos:
    print("puedes comprar los repuestos pero no te sobran creditos")
else:
    print("no tienes suficientes creditos para comprar los repuestos")


tipo_repuesto = input("Ingrese el tipo de repuesto (motor, ala, escudo): ")
if tipo_repuesto == "motor" and creditos >= precio_repuestos and tipo_repuesto == "ala":
    print("puedes comprar el repuesto Y te sobran creditos ")
elif tipo_repuesto == "ala" and creditos >= precio_repuestos :
    print("puedes comprar el repuesto y te sobran creditos")
elif tipo_repuesto == "escudo" and creditos >= precio_repuestos:
    print("puedes comprar el repuesto y te sobran creditos")
else:
    print("Tipo de repuesto no es valido")



print("ingrese el peso del tanque:")
peso_tanque = float(input())
print("Zona de destino (ingrese un numero del 1 al 3):")
zona_destino = input()

if zona_destino == "1":
    print("el precio del envio  es de $5 dolares por kilo")
    precio_envio = 5 * peso_tanque
    print("el precio del envio es de:", precio_envio)
elif zona_destino == "2":
    print("el precio del envio es de $7.50 dolares por kilo")
    precio_envio = 7.50 * peso_tanque
    print("el precio del envio es de:", precio_envio)
elif zona_destino == "3":
    print("el precio del envio es de $10 dolares por kilo")
    precio_envio = 10 * peso_tanque
    print("el precio del envio es de:", precio_envio)
else:
    print("error el numero de destino no vale")
    