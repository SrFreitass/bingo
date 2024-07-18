import socket
import tkinter as tk
from tkinter import *
from json import *
import time
import tkinter.messagebox

class Socket_member:
    def execute(addr: str, port: int):
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            client_socket.connect((addr, int(port)))
            wrote = False  
            draw_numbers_w = open("./client/database/draw_numbers.json", "w")
            draw_numbers_w.write("[]")
            draw_numbers_w.close()
            
            while True:
                try:
                    msg = client_socket.recv(2048).decode()
                    if not wrote:
                        time.sleep(1)
                        local_db = open("./client/database/matrix.json", "w")
                        local_db.write(msg)
                        local_db.close()
                        wrote = True
                    else:
                        draw_numbers_json = open("./client/database/draw_numbers.json")
                        draw_numbers: list[int] = load(draw_numbers_json)

                        if draw_numbers != msg:
                            draw_numbers_w = open("./client/database/draw_numbers.json", "w")
                            draw_numbers_w.write(msg)
                            draw_numbers_w.close()

                        status_json = open("./client/database/status.json")
                        status = load(status_json)

                        if status["winner"]:    
                            client_socket.send(status_json.read().encode())

                        status_json.close()
                        

                        draw_numbers_json.close()
                except KeyError:
                    print(KeyError, "err")
        except KeyError as e:
            tkinter.messagebox.showerror("Servidor indisponível!", "O servidor que tentou conectar não existe ou está indisponível")
            print("Ocorreu um erro ao conectar!\n")

