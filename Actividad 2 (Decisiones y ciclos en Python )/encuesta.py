#P8. Encuesta de preferencias
#Solicita edad y respuesta a la pregunta: “¿Te gusta programar?” (sí/no). 
#El programa debe repetirse mientras la edad ingresada sea mayor a cero. 
#Al finalizar, muestra cuántas respuestas fueron afirmativas y cuántas negativas.
#Controla respuestas vacías o incorrectas dentro del ciclo.

edades = []
respuestas = []

while True:

    edad = int(input("Ingresa tu edad:"))

    if edad > 0:
        edades.append(edad)
        encuesta =input("¿Te gusta programar? (Si / No)").lower()
        respuestas.append(encuesta)
    else:
        break

total_si = respuestas.count("si")
total_no = respuestas.count("no")

print(f"Cantidad de afirmaciones negativas: {total_no}")
print(f"Cantidad de afirmaciones positivas: {total_si}\n")


