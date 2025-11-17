#P6. Análisis numérico
#Solicita tres números enteros y determina:

#Si los tres son positivos.
#Si al menos uno es negativo.
#Si exactamente uno es cero.
#Debe analizar todas las combinaciones mediante condiciones encadenadas.

num1 = int(input("Ingresa el primer numero:"))
num2 = int(input("Ingresa el segundo numero:"))
num3 = int(input("Ingresa el tercer numero:"))

contador_ceros = 0

if num1 == 0:
    contador_ceros += 1

if num2 == 0:
    contador_ceros += 1

if num3 == 0:
    contador_ceros += 1

if num1 > 0 and num2 > 0 and num3 > 0:
    print("Los tres numeros son positivos")

if num1 < 0 or num2 < 0 or num3 < 0:
    print("Hay al menos un numero negativo")

if contador_ceros == 1:
    print("Hay exactamente un cero")