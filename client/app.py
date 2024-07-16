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
            numbers_json_w = open("./db/draw_numbers.json", "w")
            numbers_json_w.write("[]")
            numbers_json_w.close()
            # db = sqlite3.connect("./db/server.db")
            # cur = db.cursor()
            wrote = False  
            
            while True:
                # time.sleep(1)
                try:    
                    while True:
                        numbers_json = open("./db/draw_numbers.json")
                        client_socket.send(numbers_json.read().encode())
                        numbers_json.close()
                        time.sleep(1)
                    # draw_numbers_json = open("./db/draw_numbers.json")
                    # nums = draw_numbers_json.read()
                    # print(nums.encode(), "nuuuums")
                    # client_socket.send(nums.encode())
                    # draw_numbers_json.close()
                
                    # while True:
                        
                    # if not wrote:
                    #     local_db = open("db/matrix.json", "w")
                    #     local_db.write(msg)
                    #     local_db.close()
                    #     wrote = True
                    # else:
                    #     print("Não precisamos mais escrever a matriz")
                except KeyError:
                    client_socket.close()
                    print(KeyError, "OCORREU UM ERRO!")
                    # print("Ocorreu um erro!")
        except KeyError as e:
            print(e)
            print("Ocorreu um erro ao conectar!\n")
            client_socket.close()

