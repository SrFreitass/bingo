from tkinter import *
import threading
from client.app import Socket_client
from gui.admin_bingo import Admin_bingo

class Staff_page():
    def mount(window: Tk, res: str = "560x400"):
        w, h = res.split("x")
        text = Label(window, text="Insira a URL do servidor", font=("Arial", 18), fg="white", bg="#d98900")
        text.place(x=int(w)/2-85, y=(int(h)/2)+60)
        server_url = Entry(window, width=40)
        server_url.place(x=int(w)/2-125, y=(int(h)/2)+110)

        def initialize(addr: str, components: list):
            add = addr.split(":")
            print(add)

            thread = threading.Thread(target=Socket_client.execute, args=(add[0], add[1]))
            thread.start()

            for x in components:
                if(x):
                    x.destroy()

            Admin_bingo.mount(window, res)

        bt = Button(window, text="Iniciar", font=("Arial", 18), command=lambda: initialize(server_url.get(), [bt, server_url, text]), bg="#ffb12b")
        bt.place(x=int(w)/2-15, y=(int(h)/2)+145)