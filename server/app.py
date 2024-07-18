import socket
from json import *
from core.table_bingo import Table_Bingo
import time
import threading
class Socket_server:
    def execute(addr, port):
        clients = []
        print("Log: New Thread")
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        letters = {
            "B": [1, 15],
            "I": [16, 30],
            "N": [31, 45],
            "G": [46, 60],
            "O": [61, 75],
        }

        new_table = Table_Bingo(letters)

        try:
            server.bind((addr, int(port)))
            server.listen()
        except:
            print("Ocorreu um erro na inicialização")

        while True:
            con, addr = server.accept()
            user_table = new_table.execute()

            print("LOG: Nova conexão")
            clients.append([con, user_table])
            con.send(dumps(user_table).encode())

            thread = threading.Thread(target=receiveMessage, args=[con, len(clients)-1, clients])
            thread.start()


def receiveMessage(client, index, clients):
    while True:
        try:
            msg = client.recv(2048)
            print("MENSAGEM DOS CABAS", msg.decode())

            try:
                msg_json: dict | list[int] = loads(msg.decode())
                if type(msg_json) == "dict" and msg_json.get("win"):
                    print(msg_json.get("name"))
                    print("GANHOU!")

                for c in clients:
                    c[0].send(msg)
                print(client, msg)
            
            except:
                clients.pop(index)
                client.close()
                print("LOG: OCORREU UM ERRO")
    
        except:
            clients.pop(index)
            client.close()

