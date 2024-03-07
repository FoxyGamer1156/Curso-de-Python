clave = str(input("Pon tu contraseña para guardar:"))
intentos = 3
if len(clave) <= 1:
    print("Rellena la contraseña")
    exit()
while intentos != 0:
    contraseña = input("Introduzca su contraseña: ")
    if clave == contraseña:
        print("¡Las contraseñas coinciden!")
        break
    else:
        print("¡Contraseña incorrecta!")
        intentos = intentos - 1
        if intentos == 0:
            print("Te has quedado sin intentos, prueba mas tarde")
        print("Tienes ", intentos)