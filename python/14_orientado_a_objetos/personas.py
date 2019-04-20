
class Persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad

    def decir_hola(self):
        print("hola mi nombre es {} y yo tengo {} años".format(self.nombre,self.edad))

if __name__ == "__main__":
    person=Persona("victor",29)
    print("\n propiedad edad: {}".format(person.edad))
    
    person.decir_hola()
