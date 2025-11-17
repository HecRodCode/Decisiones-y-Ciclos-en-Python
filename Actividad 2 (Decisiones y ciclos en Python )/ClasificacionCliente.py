# P7. Clasificación de cliente
# Pide el valor total de una compra y el tipo de membresía. Clasifica al cliente como:

# Premium → monto alto y membresía activa.
# Frecuente → monto medio o membresía temporal.
# Regular → cualquier otro caso.
# Si el monto es inválido, muestra un mensaje de error.

membresia = input("Ingrese su tipo de membresia (Activa o Temporal):").lower()

while True:
    compra = int(input("Ingrese el total de la compra:"))
    if compra < 0:
        print("Monto no valido.")
    else:
        break

if compra >= 100000 and membresia == "activa":
    print("Eres cliente premium.")
elif compra >= 50000 or membresia == "temporal":
    print("Eres cliente frecuente.")
else:
    print("Eres cliente regular.")
