import tkinter as tk
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
        window.title(self.name)
        window.geometry(self.res)
        
        background = PhotoImage(file="./bg.png")

        bg_image = Label(window, image=background)
        bg_image.place(x=0, y=0, relheight=1, relwidth=1)

        

        org = Button(window, text="Organizador", font=("Arial", 18))
        part = Button(window, text="Participante", font=("Arial", 18))
        org.grid(row=0, column=0)
        w, h = self.res.split("x")
        org.place(x=int(w)/2, y=(int(h)/2)+250)
        part.place(x=int(w)/2, y=(int(h)/2)+300)
        
        
    
        
        if(0):
            length = len(self.matrix)
            
            count = 0

            for x in ["B", "I", "N", "G", "O"]:
                text = Label(window, text=x, font=("Arial", 24), borderwidth=1)
                text.grid(row=0, column=count, padx=35, pady=10)
                count+=1

            for x in range(length):
                column=x
                for y in range(length):
                    text = Label(window, text=self.matrix[x][y], font=("Arial", 24), borderwidth=1)
                    text.grid(row=y+1, column=column, padx=35, pady=10)
                    

            text = Label(window, text="Número sorteado: ", font=("Arial", 12))
            text.place(x=150, y=375)

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
                            circle.grid(row=y+1, column=column, padx=35, pady=10)    



            button = Button(window, text="Sortear", command=callback, font=("Arial", 18))
            button.place(x=40, y=375)


        # Start tkinter
        window.mainloop()
