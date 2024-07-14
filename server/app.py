import socket
from json import *
from core.table_bingo import Table_Bingo
import time
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
            clients.append((con, user_table))
            con.send(dumps(user_table).encode())

            # while True:
            #     time.sleep(0.8)
            #     try:
            #         con.send(dumps('{"hello": "world"}').encode())
            #         db.execute("SELECT * FROM draw_numbers")
            #         print(cur.fetchall(), "blá")
            #     except KeyError:
            #         print(KeyError)
            #         print("OCORREU UM ERRO!")
            # while True:
            #     time.sleep(0.7)
            #     con.send(dumps('{ "hello": "world" }').encode())
            while True:
                msg = con.recv(2048)
                if not msg: break
                print(con, msg)
            con.close()


        

