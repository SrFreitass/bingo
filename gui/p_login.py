from tkinter import *
from gui.member import Member_page
from gui.staff import Staff_page

class Login:
    def mount(self, window: Tk, res: str = "560x400"):
        w, h = res.split("x")

        def option_callback(type: str, components: list[Button]):
            # Desmount
            for x in components: x.destroy()

            if type == "PAR":
                Member_page.mount(window=window)
            elif type == "ORG":
                Staff_page.mount(window=window)
                

        background = PhotoImage(file="./gui/assets/images/bg.png")
        bg_image = Label(window, image=background)
        bg_image.img = background
        bg_image.place(x=0, y=0, relheight=1, relwidth=1)

        staff = Button(window, text="Organizador", command=lambda: option_callback("ORG", [staff, member]), font=("Arial", 18))
        member = Button(window, text="Participante ", command=lambda: option_callback("PAR", [member, staff]), font=("Arial", 18))

        staff.place(x=int(w)/2-80, y=(int(h)/2)+20)
        member.place(x=int(w)/2-80, y=(int(h)/2)+80)
