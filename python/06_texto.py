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