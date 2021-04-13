#Esto es una funcion recursiva, lo que la define es que se llama a si misma. A nivel de codigo
#es elegante, pero a nivel de efciciencia es poco eficiente.
#Lo importante es que no se hagan llamadas a la función hasta el infinito.

def retrocontador(e):
    print("{},".format(e), end="")
    
    if e > 0:   
        retrocontador(e-1)

retrocontador(10)


