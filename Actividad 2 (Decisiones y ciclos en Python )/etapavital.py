# P1. Etapa vital y formativa
# Solicita la edad y el nivel educativo de una persona. Clasifica su etapa según las siguientes reglas:

# Menor de 6 años → Infante
# Entre 6 y 17 años y estudia → Estudiante escolar
# Entre 18 y 25 años y estudia → Universitario
# Mayor de 25 años y trabaja → Adulto activo
# Mayor de 60 años y no trabaja → Adulto mayor jubilado
# En cualquier otro caso → No determinado

# Valida que la edad sea coherente y utiliza condiciones encadenadas con operadores lógicos.

while True:
    edad = (input("Ingrese su edad:"))
    if not edad.isnumeric():
        print("Ingrese una edad valida.")
    else:
        break

edad = int(edad)

if edad < 6:
    print("Eres un infante")
    exit()

situacion = input("¿Cual es tu situación actual (Estudio / Trabajo / Ambas / Ninguna)?").lower()

if 6 <= edad <= 17 and situacion == "estudio":
    print("Eres estudiante escolar")
elif 18 <= edad <= 25 and situacion == "estudio":
    print("Eres universitario")
elif edad > 25 and situacion == "trabajo":
    print("Eres un adulto activo")
elif edad < 60 and situacion == "ninguna":
    print("Eres un adulto desempleado")
elif edad > 60 and situacion == "ninguna":
    print("Eres un adulto mayor jubilado")
else:
    print("No determinado")

