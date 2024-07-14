from tkinter import *
import threading
from server.app import Socket_server
#from playsound import playsound
from generate_nums import Generate_num
from json import *
import sqlite3

class Server_bingo:
    def mount(window: Tk, res: str = "560x400"):
        w, h = res.split("x")
        drawn = []
        num = 1
       
        circle = Canvas(bd=0, highlightthickness=0, width=100, height=100, bg="orange", borderwidth=2)
        circle.create_oval(15, 15, 80, 80, fill="blue", outline="white")
        circle.place(relx=0.5, rely=0.7, anchor="center")
        num_label = Label(window, text=num, font=("Comic Sans MS", 22, "bold"), bg="blue", fg="white")
        num_label.place(relx=0.49, rely=0.69, anchor="center")        

        text = Label(window, text="Utimo número sorteado", font=("Arial", 18), bg="#ffb12b")
        text.place(relx=0.5, rely=0.55, anchor="center")