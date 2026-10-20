#OPERADORES 
"""
Operadores Aritméticos
+  Suma
-  Resta
*  Multiplicación
/  División
// División entera
%  Módulo
** Potencia
"""
valor1 = 10
valor2 = 3
suma = valor1 + valor2
resta = valor1 - valor2
multiplicacion = valor1 * valor2
division = valor1 / valor2
modulo = valor1 % valor2
potencia = valor1 ** valor2

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("Módulo:", modulo)
print("Potencia:", potencia)

print("Tabla de multiplicar del 5:")
multiplicador = 5
print("5 x 1 =", 5 * 1)
print("5 x 2 =", 5 * 2)
print("5 x 3 =", 5 * 3)
print("5 x 4 =", 5 * 4)
print("5 x 5 =", 5 * 5)
print("5 x 6 =", 5 * 6)
print("5 x 7 =", 5 * 7)
print("5 x 8 =", 5 * 8)
print("5 x 9 =", 5 * 9)
print("5 x 10 =", 5 * 10)

print("Area de un triángulo con base 5 y altura 10:", (5 * 10) / 2)

#operadores de comparación
"""
- == (igual)
- != (distinto)
- > (mayor que)
- < (menor que)
- >= (mayor o igual que)
- <= (menor o igual que)
"""

velocidad_anakin = 100
velocidad_sebulba = 80

print("¿Anakin es más rápido que Sebulba?", velocidad_anakin > velocidad_sebulba)
print("¿Anakin es más lento que Sebulba?", velocidad_anakin < velocidad_sebulba)
print("¿Anakin es igual de rapido que Sebulba?", velocidad_anakin == velocidad_sebulba)
print("¿Anakin es distinto a Sebulba?", velocidad_anakin != velocidad_sebulba)
print("¿Anakin es mas rapido o igual a Sebulba?", velocidad_anakin >= velocidad_sebulba)
print("¿Anakin es lento o igual a Sebulba?", velocidad_anakin <= velocidad_sebulba)

resultado = velocidad_anakin > velocidad_sebulba
print("Resultado de la comparación:", resultado)
print("Tipo de resultado:", type(resultado))

#operadores lógicos
"""
- and (y)
- or (o)
- not (no)
"""


motores_funcionando = True
escudos_activados = False

print("¿todos los sistemas están operativos?", motores_funcionando and escudos_activados)
print("¿Algunos sistemas estan funcionado?", motores_funcionando or escudos_activados)
print("¿Los motores no están funcionando?", not motores_funcionando)

cantidad_motores = 2
cantidad_alas = 4
combustible = 80

print("¿La nave tiene almenos 2 motores y 4 alas?")
print(cantidad_motores >= 2 and cantidad_alas >= 4 and combustible > 50)
print("¿La nave tiene almenos 2 motores o 4 alas?")
print(cantidad_motores >= 2 or cantidad_alas >= 4 or combustible > 50)
print("¿La nave no tiene almenos 2 motores?")
print(not cantidad_motores >= 2 and combustible > 50 and cantidad_alas >= 4)

#operadores de asignación
"""
- =  Asignación
- +=  Suma y asignación
- -=  Resta y asignación
- *=  Multiplicación y asignación
- /=  División y asignación
- //= División entera y asignación
- %=  Módulo y asignación
- **= Potencia y asignación
"""
velocidad = 100
print("Velocidad inicial:", velocidad)
velocidad += 50
print("Velocidad después de acelerar:", velocidad)
velocidad -= 30
print("Velocidad después de frenar:", velocidad)
multiplicador = 2
velocidad *= multiplicador
print("Velocidad después de multiplicar:", velocidad)
divisor = 4
velocidad /= divisor
print("Velocidad después de dividir:", velocidad)
modulo = 7
velocidad %= modulo
print("Velocidad después de aplicar módulo:", velocidad)
velocidad **= 2
print("Velocidad después de aplicar potencia:", velocidad)

#PRESENCIA DE OPERADORES 
"""
1. ()
2. ** (potencia)
3. * / // % (multiplicación, división, división entera, módulo)
4. + - (suma, resta)
"""
resultado_1 =  10 + 5 * 2
print("Resultado 1:", resultado_1)
resultado_2 = (10 + 5) * 2
print("Resultado 2:", resultado_2)
resultado_3 = 10 + 5 ** 2
print("Resultado 3:", resultado_3)