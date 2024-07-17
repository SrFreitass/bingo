import socket
import tkinter as tk
from tkinter import *
import time
from json import *
class Socket_client:
    def execute(addr: str, port: int):
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            client_socket.connect((addr, int(port)))
            numbers_json_w = open("./db/draw_numbers.json", "w")
            numbers_json_w.write("[]")
            numbers_json_w.close()
          
            while True:
                try:    
                    numbers_json = open("./db/draw_numbers.json")
                    client_socket.send(numbers_json.read().encode())
                    numbers_json.close()
                    time.sleep(1)
                except KeyError as e:
                    client_socket.close()
                    print(e, "OCORREU UM ERRO!")
        except KeyError as e:
            print(e)
            print("Ocorreu um erro ao conectar!\n")
            client_socket.close()

