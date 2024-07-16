from tkinter import *
from json import *
import os
import time
import time

class Member_table:
    def mount(window: Tk, res: str = "560x400"):
        w, h = res.split("x")
        last_modified = os.path.getmtime("./db/matrix.json")
        while True:
            current_modified = os.path.getmtime("./db/matrix.json")
            if current_modified != last_modified:
                break
            time.sleep(0.7)
        
        matrix_json = open("./db/matrix.json")
        matrix = loads(matrix_json.read())
        matrix_json.close()
        length = len(matrix)

        count = 0

        def mark_callback(event:Event):
            draw_numbers_json = open("./client/database/draw_numbers.json")
            draw_numbers = load(draw_numbers_json)
            draw_numbers_json.close()

            #COLUMN, ROW
            y, x = event.widget.winfo_name().split(":")

            


            if event.widget["text"] in draw_numbers:
                event.widget.config(bg="red")
            else:
                print("Impossível marcar número não sorteado!")


        for x in ["B", "I", "N", "G", "O"]:
            text = Label(window, text=x,font=("Comic Sans MS", 30, "bold"), borderwidth=1,width=4,bg="orange", fg="white")
            text.grid(row=1, column=count+2, padx=14,pady=10)
            count+=1

        for x in range(length):
            column=x
            for y in range(length):
                item = Label(window, text=matrix[x][y], relief="solid",width=4, pady=5, name=f"{y}:{x}",font=("Comic Sans MS", 30), bg="gray", fg="white")
                item.bind("<Button-1>", mark_callback)
                item.grid(row=y+2, column=column+2, padx=14, pady=1)
            
        text = Label(window, text="Ultimo número sorteado: ", font=("Comic Sans MS", 12))
        text.place(x=17, y=450)