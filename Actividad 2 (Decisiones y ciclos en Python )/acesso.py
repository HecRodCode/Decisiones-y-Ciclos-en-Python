# P3. Control de acceso
# Pide un nombre de usuario y un código numérico. 
# Permite el ingreso solo si el usuario no está en la lista restringida
# y su código cumple al menos una de las siguientes condiciones:

# Es múltiplo de 2.
# Termina en 7.
# Debe mostrar un mensaje distinto según el motivo del rechazo. 
# Elabora un diagrama de flujo que represente la decisión principal.

restringidos = ["sara", "mario", "laura"]

usuario = input("Ingrese su nombre de usuario: ").lower()
codigo = input("Ingrese su código numérico: ")

if not codigo.isnumeric():
    print("Acceso denegado: el código debe ser numérico")
else:
    codigo = int(codigo)

    if usuario in restringidos:
        print("Acceso denegado: usuario restringido")
    else:
        ultimo_digito = codigo % 10
        multiplo_de_dos = (codigo % 2 == 0)

        if multiplo_de_dos:
            print("Acceso concedido: el código es múltiplo de 2")
        elif ultimo_digito == 7:
            print("Acceso concedido: el código termina en 7")
        else:
            print("Acceso denegado: el código no cumple ningún requisito")
