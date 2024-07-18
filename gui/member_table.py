from tkinter import *
from json import *
import os
import time
import time
import tkinter
import tkinter.messagebox

class Member_table:
    def mount(window: Tk, res: str = "560x400", name: str = "user"):
        w, h = res.split("x")
        last_modified = os.path.getmtime("./client/database/matrix.json")
        while True:
            current_modified = os.path.getmtime("./client/database/matrix.json")
            if current_modified != last_modified:
                break
            time.sleep(0.7)
        
        matrix_json = open("./client/database/matrix.json")
        matrix: list[list[int]] = loads(matrix_json.read())
        matrix_json.close()
        length = len(matrix)

        count = 0

        def mark_callback(event:Event):
            draw_numbers_json = open("./client/database/draw_numbers.json")
            draw_numbers = load(draw_numbers_json)
            draw_numbers_json.close()

            #COLUMN, ROW
            y, x = event.widget.winfo_name().split(":")

            matrix[int(x)][int(y)] = "x"  

            if event.widget["text"] in draw_numbers:
                event.widget.config(bg="red")

                k = {}
                for col in matrix:
                    j = 0

                    for l in range(len(matrix)):
                        if not k.get(str(l)):
                            k[str(l)]=0 

                        if col[l] == "x" or col[l] == "*":
                            k[str(l)]+=1

                    for item_col in col:
                            if item_col == "x" or item_col == "*":
                                j+=1

                    if j == 5 or k["0"] == 5 or k["1"] == 5 or k["2"] == 5 or k["3"] == 5 or k["4"] == 5:
                        print("GANHOU!")
                        status = open("./client/database/status.json", "w")
                        a = {
                            "name": name,
                            "winner": True,
                        }  
                        status.write(dumps(a))
                        status.close()
                        tkinter.messagebox.showinfo("Parabéns!", "Você ganhou o bingo!")    
                        break
            else:
                tkinter.messagebox.showerror("ERRO!", "Impossível marcar um número que não foi sorteado!")


        for x in ["B", "I", "N", "G", "O"]:
            text = Label(window, text=x,font=("Comic Sans MS", 30, "bold"), borderwidth=1,width=4,bg="orange", fg="white")
            text.grid(row=1, column=count+2, padx=14,pady=10)
            count+=1

        for x in range(length):
            column=x
            for y in range(length):
                item = Label(window, text=matrix[x][y], relief="solid",width=4, pady=5, name=f"{y}:{x}",font=("Comic Sans MS", 30), bg="gray", fg="white")
                item.bind("<Button-1>", mark_callback)      
                item.grid(row=y+2, column=column+2, padx=14, pady=5 )
            