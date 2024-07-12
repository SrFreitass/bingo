from tkinter import *
import threading
from server.app import Socket_server
from playsound import playsound
from generate_nums import Generate_num


class Admin_bingo:
    def mount(window: Tk, res: str = "560x400"):
        w, h = res.split("x")
        window.wm_attributes("-transparentcolor", "purple")
        drawn = []
        nums = Generate_num(drawn=drawn, min_n=1, max_n=75)

        def draw_numbers():
            num = nums.execute()
            circle = Canvas(bd=0, highlightthickness=0, width=100, height=100, bg="purple")
            circle.create_oval(10, 10, 80, 80, fill="blue")
            circle.place(x=int(w)/2-40, y=(int(h)/2)+100)

        text = Label(window, text="Utimo número sorteado", font=("Arial", 18), bg="#ffb12b")
        text.place(x=int(w)/2-100, y=(int(h)/2)+60)

        bt = Button(window, text="Sortear", font=("Arial", 18), command=lambda: draw_numbers(), bg="#ffb12b")
        bt.place(x=int(w)/2-40, y=(int(h)/2)+220)