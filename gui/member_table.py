from tkinter import *
from json import *
import os
import time
import time
import tkinter
import tkinter.messagebox
from customtkinter import *

class Member_table:
    def mount(window: Tk, res: str = "560x400", name: str = "user", logo: CTkLabel = None):
        w, h = res.split("x")

        if logo:
            logo.destroy()
        

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

            matrix[int(y)][int(x)] = "x"  

            if event.widget["text"] in draw_numbers:
                event.widget.config(bg="red")

                win = False

                for i in range(length):
                    # Columns
                    if matrix[i][0] == "x" and matrix[i][1] == "x" and (matrix[i][2] == "x" or matrix[i][2] == "*") and matrix[i][3] == "x" and matrix[i][4] == "x":
                        win = True
                        break
                
                    # Rows
                    if matrix[0][i] == "x" and matrix[1][i] == "x" and (matrix[2][i] == "x" or matrix[2][i] == "*") and matrix[3][i] == "x" and matrix[4][i] == "x":
                        win = True
                        break

                # Diagonals
                if matrix[0][0] == "x" and matrix[1][1] == "x" and (matrix[2][2] == "x" or matrix[2][2] == "*") and matrix[3][3] == "x" and matrix[4][4] == "x":
                    win = True

                if matrix[0][4] == "x" and matrix[1][3] == "x" and (matrix[2][2] == "x" or matrix[2][2] == "*") and matrix[3][1] == "x" and matrix[4][0] == "x":
                    win = True
                    
                if win:
                    print("GANHOU!")
                    tkinter.messagebox.showinfo("Parabéns!", f"{name}, Você ganhou o bingo!")
                
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
            