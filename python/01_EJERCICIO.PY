print("ingrese el peso del paquete:")
peso_paquete = float(input())
print("Zona de destino (ingrese un numero del 1 al 3):")
zona_destino = input()

if zona_destino == "1":
    print("el precio del envio  es de $5 dolares por kilo")
    precio_envio = 5 * peso_paquete
    print("el precio del envio es de:", precio_envio)
elif zona_destino == "2":
    print("el precio del envio es de $7.50 dolares por kilo")
    precio_envio = 7.50 * peso_paquete  
    print("el precio del envio es de:", precio_envio)
elif zona_destino == "3":
    print("el precio del envio es de $10 dolares por kilo")
    precio_envio = 10 * peso_paquete
    print("el precio del envio es de:", precio_envio)
else:
    print("error el numero de destino no vale")
    