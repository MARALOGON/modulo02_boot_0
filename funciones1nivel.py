def normal(x):
    return x

def cuadrado(y):
    return y * y

def sumaTodos(limitTo, f):
    resultado = 0
    for i in range(limitTo+1):
        resultado += f(i)
    
    return resultado



if __name__ == '__main__':
    print(sumaTodos(100, normal))
    print(sumaTodos(3, cuadrado))