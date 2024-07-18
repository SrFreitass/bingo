from tkinter import *
import threading
from server.app import Socket_server
#from playsound import playsound
from generate_nums import Generate_num
from json import *
from customtkinter import *
import sqlite3

class Admin_bingo:
    def mount(window: Tk, res: str = "560x400"):
        w, h = res.split("x")
        drawn = []
        nums = Generate_num(drawn=drawn, min_n=1, max_n=75)

        def draw_numbers(): 
            db = open("db/draw_numbers.json")
            last_nums: list[int] = load(db)            
            print(last_nums)
            db.close()
            db_w = open("db/draw_numbers.json", "w")


            if(len(last_nums) >= 75):
                print("Limite")
                db_w.write("[]")
                db_w.close()
            else:
                num = nums.execute()
                circle = CTkCanvas(bd=0, highlightthickness=0, width=100, height=100, bg="#242424")
                circle.create_oval(15, 15, 80, 80, fill="orange", outline="white")
                num_label = CTkLabel(window, text=num, font=("Comic Sans MS", 22, "bold"), bg_color="orange")
                num_label = CTkLabel(window, text=num, font=("Comic Sans MS", 22, "bold"), bg_color="orange")
                last_nums.append(num)
                db_w.write(dumps(last_nums))
                db_w.close()
                circle.place(relx=0.5, rely=0.5, anchor="center")
                num_label.place(relx=0.5, rely=0.49, anchor="center")               
                

        text = CTkLabel(window, text="Utimo número sorteado", font=("Arial", 18))
        text.place(relx=0.5, rely=0.3, anchor="center")

        bt = CTkButton(window, text="Sortear", font=("Arial", 18), command=draw_numbers)
        bt.place(relx=0.5, rely=0.7, anchor="center")
