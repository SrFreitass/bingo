from tkinter import *
import threading
from server.app import Socket_server
#from playsound import playsound
from generate_nums import Generate_num
from json import *
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
                print("Para que vou cagar")
                db_w.write("[]")
                db_w.close()
            else:
                num = nums.execute()
                circle = Canvas(bd=0, highlightthickness=0, width=100, height=100, bg="orange", borderwidth=2)
                circle.create_oval(15, 15, 80, 80, fill="blue", outline="white")
                num_label = Label(window, text=num, font=("Comic Sans MS", 22, "bold"), bg="blue", fg="white")
                num_label = Label(window, text=num, font=("Comic Sans MS", 22, "bold"), bg="blue", fg="white")
                last_nums.append(num)
                db_w.write(dumps(last_nums))
                db_w.close()
                circle.place(relx=0.5, rely=0.7, anchor="center")
                num_label.place(relx=0.49, rely=0.69, anchor="center")    
                

        text = Label(window, text="Utimo número sorteado", font=("Arial", 18), bg="#ffb12b")
        text.place(relx=0.5, rely=0.5, anchor="center")

        bt = Button(window, text="Sortear", font=("Arial", 18), command=lambda: draw_numbers(), bg="#ffb12b")
        bt.place(relx=0.5, rely=0.9, anchor="center")

        bt_reset = Button(window, text="Resetar números", font=("Arial", 18), command=lambda: draw_numbers(), bg="#ffb12b")
        bt_reset.place(relx=0.5, rely=0.98, anchor="center")