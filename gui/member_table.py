from tkinter import *
from json import *
import os
import time

class Member_table:
    def mount(window: Tk, res: str = "560x400"):
        w, h = res.split("x")
        
        last_modified = os.path.getmtime("db\matrix.json")
        while True:
            current_modified = os.path.getmtime("db\matrix.json")
            if current_modified != last_modified:
                break
            time.sleep(0.7)
        
        matrix_json = open("db\matrix.json")
        matrix = loads(matrix_json.read())
        matrix_json.close()
        length = len(matrix)

        count = 0

        for x in ["B", "I", "N", "G", "O"]:
            text = Label(window, text=x,font=("Comic Sans MS", 30, "bold"), borderwidth=1, width=4, bg="orange", fg="white")
            text.grid(row=1, column=count+2, padx=14,pady=10)
            count+=1

        for x in range(length):
            column=x
            for y in range(length):
                text = Label(window, text=matrix[x][y], relief="solid", width=4, pady=5, font=("Comic Sans MS", 30), bg="gray", fg="white")
                
                text.grid(row=y+2, column=column+2, padx=14, pady=1)
            
        text = Label(window, text="Ultimo número sorteado: ", font=("Comic Sans MS", 12))
        text.place(x=17, y=450)

        # def callback():
        #     num = gen_num()
        #     circle = Canvas()
        #     circle.create_oval(10, 10, 80, 80, outline="white", fill="blue", width=2)
        #     circle.place(x=280, y=350)
        #     num_text = Label(window, text=num, font=("Arial", 16), bg="blue", fg="#ffffff")
        #     num_text.place(x=312 if num > 10 else 319, y=380)
            
        #     for x in range(length):
        #         column=x
        #         for y in range(length):
        #             if matrix[x][y] == num or matrix[x][y] == "O":
        #                 matrix[x][y] = "O"
        #                 circle = Canvas(window, width=35, height=35, borderwidth=0, highlightthickness=0,bg="red")
        #                 circle.grid(row=y+1, column=column, padx=1)    
            



        # button = Button(window, text="Sortear", command=callback, font=("Arial", 18))
        # button.place(x=40, y=375)
