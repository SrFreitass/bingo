import socket

class Socket_client:
    def execute(addr: str, port: int):
        print(addr, port)
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            client_socket.connect((addr, int(port)))       
            while True:
                try:
                    msg = client_socket.recv(2048).decode()
                    print(msg)
                except:
                    print("Ocorreu um erro!")
        except:
            print("Ocorreu um erro ao conectar!\n")

