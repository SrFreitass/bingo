from customtkinter import *
from gui.member import Member_page
from gui.staff import Staff_page
from gui.server import Server


class Login:
    # @staticmethod
    def mount(window: CTk, res: str = "560x400"):
        w, h = res.split("x")

        def option_callback(type: str, components: list[CTkButton]):
            # Desmount
            for x in components: x.destroy()

            if type == "PAR":
                Member_page.mount(window=window)
            elif type == "ORG":
                Staff_page.mount(window=window)
            elif type == "SER":
                Server.mount(window)
                

        # background = PhotoImage(file="./gui/assets/images/bg.png")
        # bg_image = Label(window, image=background)
        # bg_image.img = background
        # bg_image.place(x=0, y=0, relheight=1, relwidth=1)

        staff = CTkButton(window, text="Organizador"    , command=lambda: option_callback("ORG", [staff, member, server]), font=("Arial", 18))
        member = CTkButton(window, text="Participante",command=lambda: option_callback("PAR", [member, staff, server]), font=("Arial", 18))
        server = CTkButton(window, text="Servidor",command=lambda: option_callback("SER", [member, staff, server]), font=("Arial", 18))

        staff.place(relx=0.5, rely=0.58, anchor=CENTER)
        member.place(relx=0.5, rely=0.67, anchor=CENTER)
        server.place(relx=0.5, rely=0.76, anchor=CENTER)
