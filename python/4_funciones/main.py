clients='pablo,ricardo,'

def crear_cliente(client_name):
    global clients
    clients+=client_name
    _poner_coma()

def _poner_coma():
    global clients
    clients+=","

def list_client():
    global clients
    print(clients)

if __name__ == '__main__':
    list_client()
    crear_cliente('david')
    list_client()