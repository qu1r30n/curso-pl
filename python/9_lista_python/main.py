import sys
clients=["pablo","ricardo"]


def crear_cliente(client_name):
    global clients
    if client_name not in clients:
        clients.append(client_name)
    else:
        print("el cliente "+ client_name +" ya existe")


def busqueda_cliente(nom_cliente):

    for cliente in clients:
        if cliente != nom_cliente:
            continue
        else:
            return True

def list_client():
    for idx, cliente in enumerate(clients):
        print("{}: {}".format(idx,cliente))

def _tomar_nombre_cliente():
    nom_cliente=None

    while not nom_cliente:
        nom_cliente= input("cual es el nombre del cliente o pon exit para salir: \n")

        if nom_cliente=="exit":
            nom_cliente=None
            break

    if not nom_cliente:
        sys.exit()

    return nom_cliente

def  _print_bienvenido():
    print("bienvenido")
    print("*"*5)
    print("que deceas hacer?")
    print("[L]eer cliente")
    print("[C]rear cliente")
    print("[E]ditar cliente")
    print("[Q]uitar cliente")
    print("[B]uscar cliente")

def edit_cliente(nom_cliente,nom_editar):
    global clients
    if nom_cliente in clients:
        index = clients.index(nom_cliente)
        clients[index]=nom_editar
    else:
        print("cliente no se encuentra")


def quitar_cliente(nom_cliente):
    global clients
    if nom_cliente in clients:
        clients.remove(nom_cliente)
    else:
        print("cliente no se encuentra")


if __name__ == '__main__':

    _print_bienvenido()
    
    comando=input()
    comando=comando.lower()

    if comando=="c":
        nom_cliente=_tomar_nombre_cliente()
        crear_cliente(nom_cliente)
        list_client()
    elif comando=="l":
        list_client()
    elif comando=="q":
        nom_cliente=_tomar_nombre_cliente()
        quitar_cliente(nom_cliente)
        list_client()
    elif comando=="e":
        nom_cliente=_tomar_nombre_cliente()
        nom_editar=input("por cual lo vas a editar: ")
        edit_cliente(nom_cliente,nom_editar)
        list_client()
    elif comando=="b":
        nom_cliente=_tomar_nombre_cliente()
        encontrado=busqueda_cliente(nom_cliente)
        if encontrado:
            print("el cliente esta en la lista de clientes")
        else:
            print("el cliente {} no esta en la lista de clientes".format(nom_cliente))
    else:
        print("opcion invalida")

