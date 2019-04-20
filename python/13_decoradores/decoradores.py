pasword="12345"

def requerimieto_pasword(func):
    def envolver():
        passw =input("cual es la contraseña? ")
        
        if passw == pasword:
            return func()
        else:
            print("la contraseña es incorrecta")

    return envolver

@requerimieto_pasword 
def nesesito_pasword():
    print("la contraseña es correcta")

def mayusculas(funcion):
    def intermedio(*args,**kwargs):
        result= funcion(*args,**kwargs)
        return result.upper()
    return intermedio

@mayusculas
def decir_mi_nombre(nombre):
    return "hola {}".format(nombre)


if __name__ == "__main__":
    print(decir_mi_nombre("vic"))