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
            while True:
                try:
                    msg = client_socket.recv(2048).decode()
                    if not wrote:
                        local_db = open("db/matrix.json", "w")
                        local_db.write(msg)
                        local_db.close()
                        wrote = True
                    else:
                        print(msg)
                        print("Não precisamos mais escrever a matriz")
                except KeyError:
                    print(KeyError, "OCORREU UM ERRO!")
        except KeyError as e:
            print(e)
            print("Ocorreu um erro ao conectar!\n")

