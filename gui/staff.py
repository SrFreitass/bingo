from tkinter import *
import threading
from client.app import Socket_client
from gui.admin_bingo import Admin_bingo
import gui.p_login


class Staff_page():
    def mount(window: Tk, res: str = "560x400"):
        w, h = res.split("x")
        text = Label(window, text="Insira a URL do servidor", font=("Arial", 18), fg="white", bg="#d98900")
        text.place(relx=0.5, rely=0.54, anchor=CENTER)
        server_url = Entry(window, width=40)
        server_url.place(relx=0.5, rely=0.62, anchor=CENTER)

        def initialize(addr: str, components: list):
            add = addr.split(":")
            print(add)

            thread = threading.Thread(target=Socket_client.execute, args=(add[0], add[1]))
            thread.start()

            for x in components:
                if(x):
                    x.destroy()

            Admin_bingo.mount(window, res)

        def back(components: list):
            for x in components:
                x.destroy()

            gui.p_login.Login.mount(window)

        bt = Button(window, text="Iniciar", font=("Arial", 18), width=12, command=lambda: initialize(server_url.get(), [bt, server_url, text]), bg="#ffb12b")
        bt.place(relx=0.5, rely=0.72, anchor=CENTER)

        bt_back = Button(window, width=12, text="< Voltar >", font= ("Arial", 18), command=lambda: back([text, bt, bt_back]))
        bt_back.place(relx=0.5, rely=0.89, anchor=CENTER)