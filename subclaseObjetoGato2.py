#Aqui vamos a crear una clase equivalente a la clase Gato

class Cat():
    def __init__(self): 
        self.nombre = None
        self.edad = None
        self.peso = None
    
    def maullar(self):
         if self.peso == None:
            print("Soy un fantasma")
         
         if self.peso >= 5:
            print("MIAU, MIAU")
         else:
            print("miau, miau")


class Gato():
    def __init__(self, n, e, p): 
        self.nombre = n
        self.edad = e
        self.peso = p
    
    def maullar(self):
         if self.peso >=5:
            print("MIAU, MIAU")
         else:
            print("miau, miau")
    
    def __str__(self):
        return "Gato {}, e: {}, p: {}".format(self.nombre, self.edad, self.peso)


class gatoCompañia(Gato):
        def __init__(self, nombre, edad, peso, amo):
            Gato.__init__(self, nombre, edad, peso)
            self.amo = amo
            self.paseando = False
        
        def __str__(self):
            return "Gato de compañía de {}".format(self, amo)
        
        def pasear(self):
            print("{} paseo con mi amo {} por la calle".format(self.nombre, self.amo))
        
        def maullar(self):
            if self.paseando:
                print("shhh, no puedo maullar")
            else:
                Gato.maullar(self)
                
        def paseando(self, valor=None): #este es un metodo que permite consultar o modificar el estado "paseando" del gatoCompañia
            if valor == None:
                return self.__paseando
            else:
                self.__paseando == valor