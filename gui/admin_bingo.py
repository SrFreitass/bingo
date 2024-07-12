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
        db = sqlite3.connect("./db/server.db")
        cur = db.cursor()
        cur.execute("DELETE FROM draw_numbers")

        def draw_numbers():
            cur.execute("SELECT * FROM draw_numbers")
            last_nums = cur.fetchall()
            print(last_nums)
            if(len(last_nums) >= 75):
                print("Para que vou cagar")
                db.close()
            else:
                num = nums.execute()
                circle = Canvas(bd=0, highlightthickness=0, width=100, height=100, bg="orange", borderwidth=2)
                circle.create_oval(15, 15, 80, 80, fill="blue", outline="white")
                circle.place(x=int(w)/2-10, y=(int(h)/2)+100)
                num_label = Label(window, text=num, font=("Comic Sans MS", 22, "bold"), bg="blue", fg="white")
                num_label.place(x=int(w)/2 + 18 if num > 10 else int(w)/2 + 25, y=(int(h)/2)+135)
                # SQL INJECTION :)
                cur.execute(f"INSERT INTO draw_numbers VALUES ({num})")

        text = Label(window, text="Utimo número sorteado", font=("Arial", 18), bg="#ffb12b")
        text.place(x=int(w)/2-80, y=(int(h)/2)+60)

        bt = Button(window, text="Sortear", font=("Arial", 18), command=lambda: draw_numbers(), bg="#ffb12b")
        bt.place(x=int(w)/2-14, y=(int(h)/2)+220)