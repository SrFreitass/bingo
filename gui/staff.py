import threading
from client.app import Socket_client
from gui.admin_bingo import Admin_bingo
import gui.menu
from customtkinter import *


class Staff_page():
    def mount(window: CTk, res: str = "560x400"):
        w, h = res.split("x")
        code = CTkEntry(window, width=350, placeholder_text="Insira o código de organizador ")
        code.place(relx=0.5, rely=0.54, anchor=CENTER)
        server_url = CTkEntry(window, width=350, placeholder_text="Insira a url do servidor")
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

            gui.menu.Login.mount(window)

        bt = CTkButton(window, text="Entrar", font=("Arial", 18), command=lambda: initialize(server_url.get(), [bt, server_url, code, bt_back]))
        bt.place(relx=0.5, rely=0.72, anchor=CENTER)

        bt_back = CTkButton(window, text="Voltar", font= ("Arial", 20), command=lambda: back([code, server_url, bt, bt_back]))
        bt_back.place(relx=0.5, rely=0.89, anchor=CENTER)