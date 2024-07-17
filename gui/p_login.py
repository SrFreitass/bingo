from tkinter import *
from gui.member import Member_page
from gui.staff import Staff_page
from gui.server import Server

class Login:
    # @staticmethod
    def mount(window: Tk, res: str = "560x400"):
        w, h = res.split("x")

        def option_callback(type: str, components: list[Button]):
            # Desmount
            for x in components: x.destroy()

            if type == "PAR":
                Member_page.mount(window=window)
            elif type == "ORG":
                Staff_page.mount(window=window)
            elif type == "SER":
                Server.mount(window)
                

        background = PhotoImage(file="./gui/assets/images/bg.png")
        bg_image = Label(window, image=background)
        bg_image.img = background
        bg_image.place(x=0, y=0, relheight=1, relwidth=1)

        staff = Button(window, text="Organizador", width=12,command=lambda: option_callback("ORG", [staff, member, server]), font=("Arial", 18))
        member = Button(window, text="Participante", width=12,command=lambda: option_callback("PAR", [member, staff, server]), font=("Arial", 18))
        server = Button(window, text="Servidor", width=12 ,command=lambda: option_callback("SER", [member, staff, server]), font=("Arial", 18))

        staff.place(relx=0.5, rely=0.6, anchor=CENTER)
        member.place(relx=0.5, rely=0.72, anchor=CENTER)
        server.place(relx=0.5, rely=0.84, anchor=CENTER)
