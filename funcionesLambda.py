from funciones1nivel import sumaTodos

print(sumaTodos(3, lambda x: x**3))

#o puede hacerse asi

from funciones1nivel import sumaTodos

doble = lambda x: x*2

print(sumaTodos(3, doble))