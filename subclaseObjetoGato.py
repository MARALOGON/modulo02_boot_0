

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
                Gato.maullar(self) #Aqui se indica el self para que cuando se le pida maullar tenga el mismo comportamiento
                