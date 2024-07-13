from tkinter import *
import threading
from server.app import Socket_server
from gui.admin_bingo import Admin_bingo
import socket

class Server:
    def mount(window: Tk,  res: str = "560x400"):
        w, h = res.split("x")
        text = Label(window, text="URL do servidor:", font=("Arial", 18), fg="white", bg="#d98900")
        url =  Label(window, text=socket.gethostbyname(socket.gethostname()),  font=("Arial", 18), fg="white", bg="#d98900")
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

            Admin_bingo.mount(window, res)

        bt = Button(window, text="Iniciar", font=("Arial", 18), command=lambda: initialize(server_url.get(), [bt, server_url, text]), bg="#ffb12b")
        bt.place(relx=.5, rely=.75, anchor="center")