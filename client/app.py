import socket
import tkinter as tk
from tkinter import *
import threading
import json
class Socket_client:
    def execute(addr: str, port: int):
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            client_socket.connect((addr, int(port)))  
            
            while True:
                try:
                    msg = client_socket.recv(2048).decode()
                    print(msg)
                    local_db = open("db/matrix.json", "w")
                    local_db.write(msg)
                    local_db.close()
                except KeyError:
                    print(KeyError)
                    print("Ocorreu um erro!")
        except:
            print("Ocorreu um erro ao conectar!\n")

