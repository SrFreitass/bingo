import tkinter as tk
import threading
from server.app import Socket_server
from client.app import Socket_client
from gui.p_login import Login
from tkinter import *


class Window():
    def __init__(self, matrix: list[list[int]], gen_num, name: str, res: str = "560x400") -> None:
        self.matrix = matrix
        self.name = name
        self.gen_num = gen_num
        self.res = res
        self.name = name
        pass

    def execute(self):
        window = Tk()
        
        window.title(self.name)
        window.geometry(self.res)
        window.resizable(False, False)

        Login.mount(window, self.res)
        
        window.mainloop()
