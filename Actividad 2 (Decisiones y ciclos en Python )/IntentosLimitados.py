#P5. Intentos limitados
#Simula un inicio de sesión con usuario y contraseña predefinidos. Permite hasta tres intentos.
#Si ambos campos están vacíos, el intento no cuenta. 
#Finaliza al alcanzar el máximo o lograr acceso exitoso. 
#Evalúa cada combinación con operadores lógicos y muestra el motivo del fallo.

datos = {
    "Hectorcito": "2342",
    "Sara123": "Jujo23",
    "Carlitos67": "6573"
}

intentos = 3
intentos_clave = 3

while True:

    usuario = input("Ingrese su usuario:")

    if usuario in datos:
        clave = input("Ingrese su clave:")
        if usuario in datos and clave == datos[usuario]:
            print("Acceso permitido")
            break

        if usuario in datos and clave != datos[usuario]:
            while True:
                intento = input(f"Contraseña incorrecta.(Intentos restantes {intentos_clave}:")
                intentos_clave -= 1
                if intentos_clave < 0:
                    print("Demasiados intentos fallidos.")
                    exit()

                if usuario in datos and intento == datos[usuario]:
                    print("Acceso permitido")
                    exit()
    else:
        print(f"Usuario incorrecto. (Intentos restantes: {intentos})")
        intentos -= 1
        if intentos < 0:
            print("Demasiados intentos fallidos")
            break