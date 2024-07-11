import tkinter as tk
import threading
from server.app import Socket_server
from client.app import Socket_client

from tkinter import *


class Window():
    def __init__(self, matrix: list[list[int]], gen_num, name: str, res: str = "560x400") -> None:
        self.matrix = matrix
        self.name = name
        self.gen_num = gen_num
        self.res = res
        self.name = name
        pass

    def execute(self):
        window = Tk()
        # window.wm_attributes("-transparentcolor", 'blue')
        window.title(self.name)
        window.geometry(self.res)
        window.resizable(False, False)
        
        background = PhotoImage(file="./bg.png")

        bg_image = Label(window, image=background)
        bg_image.place(x=0, y=0, relheight=1, relwidth=1)

        def option(type: str, components: list[Button]):
            components[0].destroy()
            components[1].destroy()

            if(type == "PAR"):
                print("Insira a url do servidor")
                text = Label(window, text="Insira a URL do servidor", font=("Arial", 18))
                text.place(x=int(w)/2-120, y=(int(h)/2)+20)

                def connection(addr: str, components: list):
                    add = addr.split(":")

                    thread = threading.Thread(target=Socket_client.execute, args=(add[0], add[1]))
                    thread.start()
                    for x in components:
                        x.destroy()


                url = Entry(window, width=60)
                url.place(x=int(w)/2-175, y=(int(h)/2)+80)

                bt = Button(window, text="Entrar", font=("Arial", 18), command=lambda: connection(url.get(), [text, url, bt]))
                bt.place(x=int(w)/2-40, y=(int(h)/2)+120)


            if(type == "ORG"):
                Label(window, text="Insira a URL do servidor", font=("Arial", 18), fg="white", bg="#d98900").place(x=int(w)/2-175, y=(int(h)/2)+20)
                server_url = Entry(window, width=60)
                server_url.place(x=int(w)/2-175, y=(int(h)/2)+60)

                def initialize(addr: str, components: list):
                    add = addr.split(":")
                    print(add)

                    thread = threading.Thread(target=Socket_server.execute, args=(add[0], add[1], self.matrix))
                    thread.start()

                    for x in components:
                        x.destroy()

                bt = Button(window, text="Entrar", font=("Arial", 18), command=lambda: initialize(server_url.get(), [bt]), bg="#ffb12b")
                bt.place(x=int(w)/2-40, y=(int(h)/2)+100)


               

        part = Button(window, text="Participante ", command=lambda: option("PAR", [part, org]), font=("Arial", 18))
        org = Button(window, text="Organizador", command=lambda: option("ORG", [org, part]), font=("Arial", 18))
    
        org.grid(row=0, column=0)
        w, h = self.res.split("x")
        org.place(x=int(w)/2-80, y=(int(h)/2)+20)
        part.place(x=int(w)/2-80, y=(int(h)/2)+80)
        
        
        if(not"aa"):
            bg_image.destroy()

            length = len(self.matrix)
            
            count = 0

            #alinhamento
            for x in range(2):
                text = Label(window, text="ﾠ",font=("Comic Sans MS", 30), borderwidth=1)
                text.grid(row=0, column=x, padx=4, pady=2)

            for x in ["B", "I", "N", "G", "O"]:
                text = Label(window, text=x,font=("Comic Sans MS", 30), borderwidth=1)
                text.grid(row=0, column=count+2, padx=1, pady=1)
                count+=1

            for x in range(length):
                column=x
                for y in range(length):
                    text = Label(window, text=self.matrix[x][y], relief="solid", width=4, pady=5, font=("Comic Sans MS", 30))
                    text.grid(row=y+1, column=column+2, padx=1, pady=1)

                    

            text = Label(window, text="Ultimo número sorteado: ", font=("Comic Sans MS", 12))
            text.place(x=60, y=435)

            def callback():
                num = self.gen_num()
                circle = Canvas()
                circle.create_oval(10, 10, 80, 80, outline="white", fill="blue", width=2)
                circle.place(x=280, y=350)
                num_text = Label(window, text=num, font=("Arial", 16), bg="blue", fg="#ffffff")
                num_text.place(x=312 if num > 10 else 319, y=380)
                    
                for x in range(length):
                    column=x
                    for y in range(length):
                        if self.matrix[x][y] == num or self.matrix[x][y] == "O":
                            self.matrix[x][y] = "O"
                            circle = Canvas(window, width=35, height=35, borderwidth=0, highlightthickness=0,bg="red")
                            circle.grid(row=y+1, column=column, padx=1)    
                    



            # button = Button(window, text="Sortear", command=callback, font=("Arial", 18))
            # button.place(x=40, y=375)


        window.mainloop()
