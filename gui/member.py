from tkinter import *
import threading
from client.member import Socket_member
from gui.member_table import Member_table

class Member_page:
    def mount(window: Tk, res: str = "560x400"):
        w, h = res.split("x")

        text = Label(window, text="Insira a URL do servidor", font=("Arial", 18))
        text.place(x=int(w)/2-120, y=(int(h)/2)+20)

        def connection(addr: str, components: list):
            add = addr.split(":")

            thread = threading.Thread(target=Socket_member.execute, args=(add[0], add[1]))
            thread.start()
            for x in components:
                x.destroy()
                
            Member_table.mount(window)



        url = Entry(window, width=60)
        url.place(x=int(w)/2-175, y=(int(h)/2)+80)

        bt = Button(window, text="Entrar", font=("Arial", 18), command=lambda: connection(url.get(), [text, url, bt]))
        bt.place(x=int(w)/2-40, y=(int(h)/2)+120)