import random

def busqueda_binaria(datos,busqueda,indice_inicial,indice_final):
    if indice_inicial>indice_final:
        return False

    mid=(indice_inicial+indice_final)//2
    
    if busqueda == datos[mid]:
        return True
    elif busqueda < datos[mid]:
        return busqueda_binaria(datos,busqueda,indice_inicial,mid-1)
    else:
        return busqueda_binaria(datos,busqueda,mid+1,indice_final)

if __name__ == "__main__":

    datos = [random.randint(0,100) for i in range(10)]
    print(datos)
    orden = sorted(datos)
    print("orden: \n{}".format(orden))
    datos.sort()
    print("datos: \n{}".format(datos))
    busqueda=int(input("que numero quieres buscar? "))
    encontrado=busqueda_binaria(datos,busqueda,0,len(datos)-1)
    print(encontrado)