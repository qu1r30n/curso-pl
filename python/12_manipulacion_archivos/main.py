import csv
import os

client_table="client.csv"
esquema_clientes=["nombre","compañia","email","position"]
clients=[]

def _inicialisacion_almacenamiento_de_clientes():
    with open(client_table,mode="r") as f:
        leer=csv.DictReader(f, fieldnames=esquema_clientes)
        for fila in leer:
            clients.append(fila)

def _guardar_cliente_almacenamiento():
    temp_nom_tab="{}.tmp".format(client_table)
    with open(temp_nom_tab,mode="w") as f:
        escribir=csv.DictWriter(f, fieldnames=esquema_clientes)
        escribir.writerows(clients)
        os.remove(client_table)
        os.rename(temp_nom_tab,client_table)


def crear_cliente(diccionario_cliente): 
    global clients
    if diccionario_cliente not in clients:
        clients.append(diccionario_cliente)
    else:
        print("el cliente "+ diccionario_cliente +" ya existe")

def busqueda_cliente(nom_cliente):

    for cliente in clients:
        if cliente != nom_cliente:
            continue
        else:
            return True

def list_client():
        print("")
        for idx, cliente in enumerate(clients):
                print("{uid}|{nombre}|{compañia}|{email}|{position}".format(
                uid = idx,
                nombre = cliente["nombre"],
                compañia = cliente["compañia"],
                email = cliente["email"],
                position = cliente["position"]))
        print("")

def _tomar_datos_cliente(dato):
    datos_2 = None

    while not datos_2:
        datos_2 =input("cual es el {} o pon exit para salir: \n".format(dato))

        if dato == "exit":
            datos_2 = None
            break

    return datos_2

def _tomar_datos_cliente_total():
    diccionario_cliente = {
        "nombre": _tomar_datos_cliente("nombre: "),
        "compañia": _tomar_datos_cliente("compañia: "),
        "email": _tomar_datos_cliente("email: "),
        "position": _tomar_datos_cliente("position: "),
    }
        
    return diccionario_cliente

def _print_bienvenido():
    print("bienvenido")
    print("*"*5)
    print("que deceas hacer?")
    print("[L]eer cliente")
    print("[C]rear cliente")
    print("[E]ditar cliente")
    print("[Q]uitar cliente")
    print("[B]uscar cliente")

def edit_cliente(id_cliente,datos_editar):
    global clients
    
    if len(clients) - 1 >= id_cliente:
        clients[id_cliente]=datos_editar

    else:
        print("")
        print("cliente no se encuentra")

def quitar_cliente(id_cliente):
    global clients
    bandera=0
    for idx,nombre_cliente in enumerate(clients):
        print(nom_cliente)
        if idx == id_cliente:
            del clients[id_cliente]
            bandera=1
            break
    if bandera==0:
        print("")
        print("cliente no se encuentra")
 

if __name__ == '__main__':
    _inicialisacion_almacenamiento_de_clientes()
    _print_bienvenido()
    
    comando = input()
    comando = comando.lower()

    if comando == "c":
        diccionario_cliente = _tomar_datos_cliente_total()
        crear_cliente(diccionario_cliente)
        list_client()
    elif comando == "l":
        list_client()
    elif comando == "q":
        id_cliente = int(_tomar_datos_cliente("id"))
        quitar_cliente(id_cliente)
        list_client()
    elif comando == "e":
        id_cliente = int(_tomar_datos_cliente("id"))
        cliente_editar = _tomar_datos_cliente_total()
        edit_cliente(id_cliente,cliente_editar)
        list_client()
    elif comando == "b":
        nom_cliente = _tomar_datos_cliente("nombre")
        encontrado = busqueda_cliente(nom_cliente)
        if encontrado:
            print("el cliente esta en la lista de clientes")
        else:
            print("el cliente {} no esta en la lista de clientes".format(nom_cliente))
    else:
        print("opcion invalida")
    _guardar_cliente_almacenamiento()
