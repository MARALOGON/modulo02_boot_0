from functools import reduce

def doble(x):
    return x+x


lista = [1, 3, -1, 15, 9]

listaDobles = map(lambda x: x*2, lista)
listaDobles1 = map(doble, lista)

def esPar(x):
    return x % 2 == 0

listaPares = filter(lambda x: x % 2 == 0, lista)
listaPares1 = filter(esPar, lista)

sumatorio = reduce(lambda x, y: x + y, lista)

suma100 = reduce(lambda x, y: x + y, range(101))



#Reduce tiene el problema de que no cuenta el primer elemento para realizar la operacion que si aplica al resto
#Por eso, el resultado de esta funcion lambda es 53 y no 54 como deberia ser
#para subsanar ese error hay que:
#1. crear una copia de la lista

l=lista[:] #Con esta sintaxis de [:] se crea una copia de todo lo que contiene la lista
#Esto sirve para clonar la lista, por si acaso volvemos a n ecesitar la original y queremos modificar la copia,,
#que la original se mantenga. Si solo asignaramos l=lista, los cambios que hicieramos en l
#tambien se harian en lista


#2. Se añade el elmento neutro para que la funcion empiece a operar en la posicion cero de la lista
l.insert(0,0)

sumatorioDobles = reduce(lambda x, y: x + y*2, l)


print(list(listaPares))
print(list(listaPares1))

print(sumatorio)
print(sumatorioDobles)


print(suma100)
