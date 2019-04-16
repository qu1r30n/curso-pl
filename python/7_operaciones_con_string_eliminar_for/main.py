clients='pablo,ricardo,'


def crear_cliente(client_name):
    global clients
    if client_name not in clients:
        clients+=client_name
        _poner_coma()
    else:
        print("el cliente "+ client_name +" ya existe")


def busqueda_cliente(nom_cliente):
    global clients
    lista_cliente=clients.split(",")

    for clients in lista_cliente:
        if clients != nom_cliente:
            continue
        else:
            return True


def _poner_coma():
    global clients
    clients+=","


def list_client():
    global clients
    print(clients)


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
        clients=clients.replace(nom_cliente + ",", nom_editar + ",")
        list_client()
    else:
        print("cliente no se encuentra")


def quitar_cliente(nom_cliente):
    global clients
    if nom_cliente in clients:
        clients=clients.replace(nom_cliente + ",", "")
        list_client()
    else:
        print("cliente no se encuentra")


if __name__ == '__main__':

    _print_bienvenido()
    
    comando=input()
    comando=comando.lower()
    if comando=="c":
        nom_cliente=input("cual es el nom del cliente: ")
        list_client()
        crear_cliente(nom_cliente)
        list_client()

    elif comando=="l":
        list_client()

    elif comando=="q":
        nom_cliente=input("cual es el nom del cliente: ")
        quitar_cliente(nom_cliente)

    elif comando=="e":
        nom_cliente=input("cual es el nom del cliente: ")
        nom_editar=input("por cual lo vas a editar: ")
        edit_cliente(nom_cliente,nom_editar)
    elif comando=="b":
        nom_cliente=input("cual es el nom del cliente: ")
        encontrado=busqueda_cliente(nom_cliente)
        if encontrado:
            print("el cliente esta en la lista de clientes")
        else:
            print("el cliente {} no esta en la lista de clientes".format(nom_cliente))
    else:
        print("opcion invalida")

