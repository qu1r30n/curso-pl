clients='pablo,ricardo,'


def crear_cliente(client_name):
    global clients
    if client_name not in clients:
        clients+=client_name
        _poner_coma()
    else:
        print("el cliente "+ client_name +" ya existe")


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
    print("[c]rear cliente")
    print("[e]editar cliente")
    print("[b]orrar cliente")

def edit_cliente(nom_cliente,nom_editar):
    global clients
    if nom_cliente in clients:
        clients=clients.replace(nom_cliente + ",", nom_editar + ",")
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
    elif comando=="b":
        pass
    elif comando=="e":
        nom_cliente=input("cual es el nom del cliente: ")
        nom_editar=input("por cual lo vas a editar: ")
        edit_cliente(nom_cliente,nom_editar)
    else:
        print("opcion invalida")

