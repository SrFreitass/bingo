import socket
import tkinter as tk
from tkinter import *
import threading
import json
import sqlite3
import time
from json import *
class Socket_client:
    def execute(addr: str, port: int):
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            client_socket.connect((addr, int(port)))
            # db = sqlite3.connect("./db/server.db")
            # cur = db.cursor()
            wrote = False  
            
            while True:
                time.sleep(1)
                try:
                    draw_numbers_json = open("./db/draw_numbers.json")
                    client_socket.sendall(draw_numbers_json.read().encode())
                    draw_numbers_json.close()
                    # msg = client_socket.recv(2048).decode()
                    # while True:
                        
                    # if not wrote:
                    #     local_db = open("db/matrix.json", "w")
                    #     local_db.write(msg)
                    #     local_db.close()
                    #     wrote = True
                    # else:
                    #     print("Não precisamos mais escrever a matriz")
                except KeyError:
                    print(KeyError, "OCORREU UM ERRO!")
                    # print("Ocorreu um erro!")
        except KeyError as e:
            print(e)
            print("Ocorreu um erro ao conectar!\n")

