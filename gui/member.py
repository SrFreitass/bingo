import threading
from client.member import Socket_member
from gui.member_table import Member_table
import tkinter.messagebox
import gui.menu
from customtkinter import *
import customtkinter
class Member_page:
    def mount(window: CTk, res: str = "560x400"):
        w, h = res.split("x")

        def connection(addr: str, components: list, username: str):
            try:
                add = addr.split(":")
                thread = threading.Thread(target=Socket_member.execute, args=(add[0], add[1]))
                thread.start()
                for x in components:
                    x.destroy()
                
                Member_table.mount(window, name=username)
            except KeyError as e:
                tkinter.messagebox.showerror("Erro ao conectar!", "Houve um erro ao tentar conectar do servidor!")

        def back(components: list):
            for x in components:
                x.destroy()
    
            gui.menu.Login.mount(window)


        input_name = CTkEntry(window, width=350,placeholder_text="Insira um apelido")
        input_name.place(relx=0.5, rely=0.51,anchor=CENTER)

        url = CTkEntry(window, width=350,placeholder_text="Insira a url do servidor")
        url.place(relx=0.5, rely=0.6,anchor=CENTER)
    

        bt = CTkButton(window, text="Entrar", font=("Arial", 18), command=lambda: connection(addr=url.get(), username=input_name.get(), components=[input_name, url, bt, bt_back]))
        bt.place(relx=0.5, rely=0.69, anchor=CENTER)
        
        bt_back = CTkButton(window, text="Voltar", font=("Arial", 18), command=lambda: back([input_name, url, bt, bt_back]))
        bt_back.place(relx=0.5, rely=0.89, anchor=CENTER)
