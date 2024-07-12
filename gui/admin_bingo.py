from tkinter import *
import threading
from server.app import Socket_server
#from playsound import playsound
from generate_nums import Generate_num
from json import *

class Admin_bingo:
    def mount(window: Tk, res: str = "560x400"):
        w, h = res.split("x")
        drawn = []
        nums = Generate_num(drawn=drawn, min_n=1, max_n=75)

        def draw_numbers():
            db_wr = open("./db/server.json", "w")
            db_re = open("./db/server.json", "r")
            last_nums: list[int] = loads(db_re.read()) if db_re.read() else []

            if(len(last_nums) >= 75):
                print("Para que vou cagar")
                db_wr.close()
                db_re.close()
            else:
                num = nums.execute()
                circle = Canvas(bd=0, highlightthickness=0, width=100, height=100, bg="orange", borderwidth=2)
                circle.create_oval(15, 15, 80, 80, fill="blue", outline="white")
                circle.place(x=int(w)/2-10, y=(int(h)/2)+100)
                num_label = Label(window, text=num, font=("Comic Sans MS", 22, "bold"), bg="blue", fg="white")
                num_label.place(x=int(w)/2 + 18 if num > 10 else int(w)/2 + 25, y=(int(h)/2)+135)
                last_nums.append(num)
                if(db_wr.writable()):
                    db_wr.write(dumps(last_nums))
                print(last_nums)
                db_wr.close()
                db_re.close()
                # db.append(num)
                # print(db)
                # server_db.write(dumps(db))
                # server_db.close()

        text = Label(window, text="Utimo número sorteado", font=("Arial", 18), bg="#ffb12b")
        text.place(x=int(w)/2-80, y=(int(h)/2)+60)

        bt = Button(window, text="Sortear", font=("Arial", 18), command=lambda: draw_numbers(), bg="#ffb12b")
        bt.place(x=int(w)/2-14, y=(int(h)/2)+220)