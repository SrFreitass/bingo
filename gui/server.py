from tkinter import *
import threading
from server.app import Socket_server
from gui.server_bingo import Server_bingo
import socket
import gui.p_login

class Server:
    def mount(window: Tk,  res: str = "560x400"):
        w, h = res.split("x")

        hostname = socket.gethostbyname(socket.gethostname())

        text = Label(window, text="URL do servidor:", font=("Arial", 18), fg="white", bg="#d98900")
        url =  Label(window, text=hostname,  font=("Arial", 18), fg="white", bg="#d98900")
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

        def back(components: list):
            for x in components:
                x.destroy()
    
            gui.p_login.Login.mount(window)

        bt = Button(window, text="Iniciar", font=("Arial", 18), command=lambda: initialize(f"{hostname}:8080", [bt]), bg="#ffb12b")
        bt.place(relx=.5, rely=.75, anchor="center")
        
        bt_back = Button(window, width=12, text="< Voltar >", font= ("Arial", 18), command=lambda: back([text, url, bt, bt_back]))
        bt_back.place(relx=0.5, rely=0.89, anchor=CENTER)