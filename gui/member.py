from tkinter import *
import threading
from client.member import Socket_member
from gui.member_table import Member_table
import tkinter.messagebox
import gui.p_login
class Member_page:
    def mount(window: Tk, res: str = "560x400"):
        w, h = res.split("x")

        def connection(addr: str, components: list):
            try:
                add = addr.split(":")
                thread = threading.Thread(target=Socket_member.execute, args=(add[0], add[1]))
                thread.start()
                for x in components:
                    x.destroy()
                
                Member_table.mount(window)
            except:
                tkinter.messagebox.showerror("Erro ao conectar!", "Houve um erro ao tentar conectar do servidor!")

        def back(components: list):
            for x in components:
                x.destroy()
    
            gui.p_login.Login.mount(window)


        label_name = Label(window, text="Qual seu apelido?", font=("Arial", 18))
        input_name = Entry(window, width=60)

        label_name.place(relx=0.5, rely=0.5,anchor=CENTER)
        input_name.place(relx=0.5, rely=0.56,anchor=CENTER)

        text = Label(window, text="Insira a url do servidor", font=("Arial", 18))
        url = Entry(window, width=60)

        text.place(relx=0.5, rely=0.63, anchor=CENTER)
        url.place(relx=0.5, rely=0.69,anchor=CENTER)
    

        bt = Button(window, width=12, text="Entrar", font=("Arial", 18), command=lambda: connection(url.get(), [text, url, bt]))
        bt.place(relx=0.5, rely=0.79, anchor=CENTER)

        bt_back = Button(window, width=12, text="< Voltar >", font=("Arial", 18), command=lambda: back([text, url, bt, bt_back]))
        bt_back.place(relx=0.5, rely=0.89, anchor=CENTER)