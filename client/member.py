import socket
import tkinter as tk
from tkinter import *
import threading
import json
import sqlite3
import time
from json import *
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
                        local_db = open("db/matrix.json", "w")
                        local_db.write(msg)
                        local_db.close()
                        wrote = True
                    else:
                        draw_numbers = open("./client/database/draw_numbers.json")
                        if load(draw_numbers) != msg:
                            draw_numbers_w = open("./client/database/draw_numbers.json", "w")
                            draw_numbers_w.write(msg)
                            draw_numbers_w.close()
                        print(msg)
                        draw_numbers.close()

                except KeyError:
                    print(KeyError, "OCORREU UM ERRO!")
        except KeyError as e:
            print(e)
            print("Ocorreu um erro ao conectar!\n")

