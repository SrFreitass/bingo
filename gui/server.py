import threading
from server.app import Socket_server
from gui.server_bingo import Server_bingo
import socket
import gui.menu
import tkinter.messagebox
import gui.menu
from customtkinter import *
import customtkinter    

class Server:
    def mount(window: CTk,  res: str = "560x400"):
        w, h = res.split("x")

        hostname = socket.gethostbyname(socket.gethostname())

        text = CTkLabel(window, text="URL do servidor:", font=("", 20))
        url =  CTkLabel(window, text=hostname, font=("", 20, "bold"))
        text.place(relx=.5, rely=.55, anchor="center")
        url.place(relx=.5, rely=.64, anchor="center")
        
        print()
        def initialize(addr: str, components: list):
            add = addr.split(":")
            print(add)

            thread = threading.Thread(target=Socket_server.execute, args=(add[0], add[1]))
            thread.start()

            for x in components:
                if(x):
                    x.destroy()
            
            bt_exit = CTkButton(window, text="Fechar", font= ("Arial", 20), command=lambda: window.quit())
            bt_exit.place(relx=0.5, rely=0.82, anchor=CENTER)


        def back(components: list):
            for x in components:
                x.destroy()
    
            gui.menu.Login.mount(window)

        bt = CTkButton(window, text="Iniciar", font=("Arial", 18), command=lambda: initialize(f"{hostname}:8080", [bt, bt_back]))
        bt.place(relx=.5, rely=.75, anchor="center")
    
        bt_back = CTkButton(window, text="Voltar", font= ("Arial", 20), command=lambda: back([text, url, bt, bt_back]))
        bt_back.place(relx=0.5, rely=0.89, anchor=CENTER)