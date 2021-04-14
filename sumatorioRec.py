#Ahora vamos a hacer un sumatorio recursivo

def sumatorio(n):
    if n != 0:
        return n + sumatorio(n-1)
    else:
        return 0 #Aqui se pone el return 0 para que no pete, ya que si siguiera haciendo la operacion
                 #sin el else, sumaria al final 1+None y eso daria error. Es interesante hacer
                 #el debug del programa para ver como funciona la recursividad.

    

print(sumatorio(4))



def factorial(n):
    if n!= 0:
        return n * factorial(n-1)
    else:
        return 1

print(factorial(5))