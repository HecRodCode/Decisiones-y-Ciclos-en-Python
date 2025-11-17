# P2. Participante elegible
# Solicita la edad, si tiene licencia de conducción y si posee vehículo propio.
# Determina si la persona puede participar en una competencia, aplicando las siguientes condiciones:

# Edad mínima de 18 años.
# Licencia vigente.
# Vehículo propio o préstamo autorizado.
# Evalúa con combinaciones de and y or para determinar si es Apto o No apto.

while True:
    edad = input("Ingrese su edad:")
    if not edad.isnumeric():
        print("Ingrese un numero valido.23")
    else:
        break

edad = int(edad)

if edad < 18:
    print("Los menores de edad no pueden participar.")
    exit()

vehiculo = input("¿Poseé vehiculo propio?:").lower()
licencia = input("¿Poseés licencia de condicuión?").lower()

if vehiculo == "si" and licencia == "si":
    print("Puedes participar en la competencia")
elif vehiculo == "si" and licencia == "no":
    print("No puedes conducir sin licencia")
elif vehiculo == "no" and licencia == "si":
    arquiler = input("¿Deseas arquilar un auto?").lower()
    if arquiler == "si":
        print("Prestamo de auto autorizado")
    else:
        print("No puedes competir sin auto.")
else:
    print("No eres apto para competir")