import os

estado = False
calefaccion = False

# Limpiar consola
def restart():
    os.system("cls")

# Menu principal
def menu_opciones():
    print("""
# ====================================== #
|                                        |
|            Menu de opciones            |
|----------------------------------------|
|                                        | 
| [1] Luces                              |
| [2] Calefacción                        |
| [3] Ver estado                         |
| [4] Salir                              |
|                                        |
# ====================================== #
    """)

# Menu de luces
def menu_luces():
    print("""
# ====================================== #
|                                        |
|            Menu de luces               |
|----------------------------------------|
|                                        | 
| [1] Encender las luces                 |
| [2] Apagar luces                       |
| [3] Ver estado                         |
| [4] Salir                              |
|                                        |
# ====================================== #
    """)

# Bucle del menu de luces
def menu_luces_loop():
    while True:
        restart()
        menu_luces()

        opcion = int(input("Ingrese una opcion:"))

        match opcion:
            case 1:
                hora = input("¿Es de dia o de noche?:").lower()
                if hora == "noche":
                    luces_encendidas_loop()
                else:
                    light_day()
            case 2:
                luces_apagadas_loop()
            case 3:
                estado_loop()
            case 4:
                break

# Menu de luces encendidas
def light_on():
    print("""
 ===============================================
|                                               |
|        LUCES ENCENDIDAS CORRECTAMENTE         |
|                                               |
 ===============================================
                    """)

# Luces encendidas
def luces_encendidas_loop():
    global estado
    estado = True
    restart()
    light_on()
    input("\nPresiona ENTER para continuar...")

# Menu de condicion - luces x dia
def light_day_menu():
    print("""
 ===============================================
|                                               |
|  LAS LUCES NO SE PUEDEN ENCERDER POR EL DIA   |
|                                               |
 ===============================================
                    """)

# Por el dia no se prenden las luces
def light_day():
    restart()
    light_day_menu()
    input("\nPresiona ENTER para continuar...")

# Menu de luces apagadas
def light_off():
    print("""
 ===============================================
|                                               |
|        LUCES APAGADAS CORRECTAMENTE           |
|                                               |
 ===============================================
                    """)

# Luces apagadas
def luces_apagadas_loop():
    global estado
    estado = False
    restart()
    light_off()
    input("\nPresiona ENTER para continuar...")

# Menu para estado de luces - encendidas
def estado_menu_on():
    print("""
 ===============================================
|                                               |
|        Estado de las luces: encendidas        |
|                                               |
 ===============================================
                    """)

# Menu para estado de luces - apagadas
def estado_menu_off():
    print("""
 ===============================================
|                                               |
|        Estado de las luces: apagadas          |
|                                               |
 ===============================================
                    """)

# Bucle del estado
def estado_loop():
    restart()
    global estado
    if estado:
        estado_menu_on()
    else:
        estado_menu_off()
    input("\nPresiona ENTER para continuar...")

# Menu de calefacion
def menu_calefaccion():
    print("""
# ====================================== #
|                                        |
|          Menu de calefacción           |
|----------------------------------------|
|                                        | 
| [1] Encender calefacción               |
| [2] Apagar calefacción                 |
| [3] Ver estado                         |
| [4] Salir                              |
|                                        |
# ====================================== #
    """)

# Bucle de menu de calefaccion
def menu_calefaccion_loop():
    global estado
    global calefaccion

    while True:
        restart()
        menu_calefaccion()

        opcion = int(input("Ingrese una opción:"))

        match opcion:
            case 1:
                temperatura = int(input("Ingrese la temperatura actual:"))
                if temperatura < 18 and estado:
                    calefaccion_on_loop()
                else:
                    temperatura_condition_loop()
            case 2:
                calefaccion_off_loop()
            case 3:
                estado_calefaccion_loop()
            case 4:
                break

# Menu de calefaccion encendida
def calefaccion_on():
    print("""
 ===============================================
|                                               |
|      CALEFACCION ENCENDIDA CORRECTAMENTE      |
|                                               |
 ===============================================
                    """)

# Bucle de calefaccion encendida
def calefaccion_on_loop():
    global calefaccion
    calefaccion = True
    restart()
    calefaccion_on()
    input("\nPresiona ENTER para continuar...")

# Menu de condicion de temperatura
def temperatura_condition_menu():
    print("""
 ================================================
|                                                |
|   ¡LA CALEFACCION SOLO SE PUEDE ENCENDER SI    |
|   LA TEMPERATURA ES MENOR QUE 18 Y LAS LUCES   |
|             ESTAN ENCENDIDAS!                  |
|                                                |
 ================================================
                    """)

# Condicion de temperatura
def temperatura_condition_loop():
    restart()
    temperatura_condition_menu()
    input("\nPresiona ENTER para continuar...")

# Menu de calefaccion apagada
def calefaccion_off():
    print("""
 ===============================================
|                                               |
|       CALEFACCION APAGADA CORRECTAMENTE       |
|                                               |
 ===============================================
                    """)

# Bucle de calefaccion apagada
def calefaccion_off_loop():
    global calefaccion
    calefaccion = False
    restart()
    calefaccion_off()
    input("\nPresiona ENTER para continuar...")

# Menu para estado de calefaccion - encendida
def estado_calefaccion_on():
    print("""
 ===============================================
|                                               |
|       Estado de calefaccion: encendida        |
|                                               |
 ===============================================
                    """)

# Menu para estado de calefaccion - apagadas
def estado_calefaccion_off():
    print("""
 ===============================================
|                                               |
|        Estado de calefaccion: apagada         |
|                                               |
 ===============================================
                    """)

# Bucle de calefaccion
def estado_calefaccion_loop():
    restart()
    global calefaccion

    if calefaccion == True:
        estado_calefaccion_on()
    else:
        estado_calefaccion_off()
    input("\nPresiona ENTER para continuar...")

# Menu para estado general
def estado_menu_general():
    print("""
 ===============================================
|                                               |
|      >> Estado de luces:                      |
|      >> Estado de calefaccion:                |
|                                               |
 ===============================================
                    """)

# Condiciones de menu de estado principal
def estado_menu_general_loop():
    global estado, calefaccion
    restart()

    if estado is False and calefaccion is False:
        estado_menu_False_False()
        input("\nPresiona ENTER para continuar...")
        return

    if estado == False and calefaccion == False:
        estado_menu_False_False()
    elif estado == True and calefaccion == False:
        estado_menu_True_False()
    elif estado == True and calefaccion == True:
        estado_menu_True_True()

    input("\nPresiona ENTER para continuar...")

# Menu para estado False - False
def estado_menu_False_False():
    print("""
 ===============================================
|                                               |
|      >> Estado de luces: apagada              |
|      >> Estado de calefaccion: apagada        |
|                                               |
 ===============================================
                    """)
# Bucle para estado False - False
def estado_menu_False_False_loop():
    restart()
    estado_menu_False_False()
    input("\nPresiona ENTER para continuar...")

# Menu para estado True - False
def estado_menu_True_False():
    print("""
 ===============================================
|                                               |
|      >> Estado de luces: encendidas           |
|      >> Estado de calefaccion: apagada        |
|                                               |
 ===============================================
                    """)
# Bucle para estado True - False
def estado_menu_True_False_loop():
    restart()
    estado_menu_True_False()
    input("\nPresiona ENTER para continuar...")

# Menu para estado True - True
def estado_menu_True_True():
    print("""
 ===============================================
|                                               |
|      >> Estado de luces: encendidas           |
|      >> Estado de calefaccion: encendida      |
|                                               |
 ===============================================
                    """)

# Bucle para estado True - True
def estado_menu_True_True_loop():
    restart()
    estado_menu_True_True()
    input("\nPresiona ENTER para continuar...")


while True:
    restart()
    menu_opciones() 

    opcion = int(input("Ingresa una opción:"))
    
    match opcion:
        case 1:
            menu_luces_loop()
        case 2:
            menu_calefaccion_loop()
        case 3:
            estado_menu_general_loop()
        case 4:
            break