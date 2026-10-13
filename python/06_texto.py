# strings cadenas de caracteres
jedi="Qui-Gon Jinn"
aprendiz ="Obi-Wan Kenobi"
droide = "R2-D2"
planeta = "Naboo"
codigo = "327"

print("Jedi:", jedi)
print("Jedi:", type(jedi))
print("Aprendiz:", aprendiz)
print("Aprendiz:", type(aprendiz))
print("Droide:", droide)
print("Droide:", type(droide))
print("Planeta:", planeta)
print("Planeta:", type(planeta))        
print("Codigo:", codigo)
print("Codigo:", type(codigo))  

longitud_jedi = len(jedi)
print("Longitud del nombre del Jedi es :"+ str(longitud_jedi))
longitud_aprendiz = len(aprendiz)
print("Longitud del nombre del Aprendiz es :"+ str(longitud_aprendiz))

mensaje = "La Federacion de Comercio ha establecido un bloque en Naboo."
print("el mensaje es:" + mensaje)
mensaje_mayusculas = mensaje.upper()
print("el mensaje en mayusculas es:" + mensaje_mayusculas)
mensaje_minusculas = mensaje.lower()
print("el mensaje en minusculas es:" + mensaje_minusculas) 

comunicado = "Los Jedi son enviados a Naboo"
print("el comunicado es:" + comunicado)
nuevo_comunicado = comunicado.replace("Naboo", "Tatooine")
print("el nuevo comunicado es:" + nuevo_comunicado)

planetas = "Naboo, Tatooine, Coruscant, Alderaan"
planetas_listas = planetas.split(", ")
print(planetas_listas)
print("La lista de planetas es:" + str(planetas_listas))
print("El primer planeta de la lista es:" + planetas_listas[0])

droide = "R2-D2"
print("El droide es:" + droide) 
print("El primer caracter del droide es:" + droide[0])  
print("El segundo caracter del droide es:" + droide[1]) 
print("El tercer caracter del droide es:" + droide[2])
print("El cuarto caracter del droide es:" + droide[3])      
print("El quinto caracter del droide es:" + droide[4])
print("El sexto caracter del droide es:" + droide[-1])

planeta = "      Naboo      "
print("El planeta es:" + planeta)
print("El planeta sin espacios es:" + planeta.strip())  
