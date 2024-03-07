'''Creacion de variables'''
lista = []
i_lista = 0
in_eli = ""

'''Bucle para insertar los 5 elementos'''
print("Inserte los elementos para la lista:")
while i_lista < 5:
    lista.insert(i_lista, input())
    i_lista += 1
    print(i_lista)

'''Bucle para añadir o eleminar elementos, enseñando siempre el cambio,
en caso de que dija 'no' rompera el bucle, dando el mensaje de despedida.'''
while in_eli != "no":
    print("\nAqui tienes tu lista:", lista, "\n")
    print("¿Quiere 'inserta' o 'eliminar' un elemento?\n")
    print("Encaso de no querer hacernada ponga 'no'\n")
    in_eli = input()
    '''Condiciones para comprobar que quiere hacer el usuario, en caso de dejar
    vacio saltara un error'''
    if in_eli == "insertar":
        print("\nInserte el elemento:")
        lista.append(input())
    elif in_eli == "eliminar":
        print("\n¿Que elemento quiere eliminar?\n")
        lista.remove(input())
    elif in_eli == "":
        print("\nError no se encontro ninguna solicitud")
print("Gracias por su visita, que tenga buen dia")