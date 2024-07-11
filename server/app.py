import socket
from json import *
from generate_cols import Generate_cols

class Socket_server:
    def execute(addr, port, matrix):
        clients = []
        print("New Thread")
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        
        try:
            server.bind((addr, int(port)))
            server.listen()

            letters = {
                "B": [1, 15],
                "I": [16, 30],
                "N": [31, 45],
                "G": [46, 60],
                "O": [61, 75],
            }

            gen_cols = Generate_cols(letters=letters, matrix=matrix)

            for x in letters.keys():
                gen_cols.execute(x)

        except:
            print("Ocorreu um erro na inicialização")

        while True:
            con, addr = server.accept()
            clients.append(con)
            print("Nova conexão")
            con.send(dumps(matrix).encode())
            
            # while True:
            #     msg = con.recv(1024)
            #     if not msg: break
            #     print(con, msg)
            # con.close()


        

