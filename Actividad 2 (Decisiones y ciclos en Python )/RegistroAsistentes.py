# P4. Registro de asistentes
# Crea un ciclo que solicite nombres hasta que se escriba “FIN”. Al finalizar, muestra:

# El total de nombres ingresados.
# Si hay nombres repetidos.
# El programa debe ignorar entradas vacías y evitar 
# usar TRY/EXCEPTION pero buscar alternativas para validaciones.

nombres = []

while True:

    nombre = input("Ingrese un nombre:")
    
    if nombre == "":
        continue

    if nombre == "FIN":
        break
    
    nombres.append(nombre)

total = 0

for nombre in nombres:
    total += 1

repetidos = 0

for nombre in nombres:
    if nombres.count(nombre) > 1:
        repetidos += 1

print(f"Total de nombres: {total}")
print(nombres)
print(f"Total de nombres repetidos: {repetidos}")
