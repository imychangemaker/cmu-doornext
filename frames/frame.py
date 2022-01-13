import tkinter as tk
from tkinter import font as tkfont
from abc import abstractmethod
from PIL import ImageTk, Image


class Frame(tk.Frame):
    def __init__(self, parent, controller):
        """Handle integration into Tkinter parent app
        """
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.var = tk.StringVar()
        self.var.set("")
        self.text_label = tk.Label(self, textvariable=self.var,
                                   font=tkfont.Font(family='Helvetica', size=18, weight="bold"),
                                   fg="#03717D")
        self.text_label.place(x=208, y=20)

    @abstractmethod
    def transition(self, address: str, local: bool):
        """Initialize Craig List
        Args:
            address (str): complete address returned from openstreetmap search.
            local (str): check if only local data should be displayed.
        """
        pass

    def _menu(self, frame: str):
        """ Method to handle menu display
            Displays correct buttons depending on the Frame you are at
        """
        if frame != "StartPage":
            self.var.set(f"Location: {self.controller.get_city()}")

        # Create canvas for menu
        self.w = tk.Canvas(width=190, height=720, highlightthickness=0, borderwidth=0)
        self.w.create_rectangle(0, 0, 190, 720, fill="#D0ECE7", outline="#D0ECE7")
        self.w.place(x=0, y=0)
        self.image = ImageTk.PhotoImage(Image.open("pics/logo.png"))
        self.w.create_image(4, 4, image=self.image, anchor='nw')
        self.w.create_text(95, 700, text="Copyright ©2021 DoorNext", font=tkfont.Font(family='Helvetica', size=9),
                           fill="#909497")

        pages = ["StartPage", "Vaccine", "Demographics", "Weather", "Acts", "AllEvents", "Housing"]
        
        self._button()
        # display extra buttons if located at specific pages
        if (frame == "AllEvents") or (frame == "Map"):
            pages = pages + ["Map"]
            button8 = tk.Button(self.w, text="Event Map", fg="#03717D", width=12, height=1,
                                command=lambda: self._go_to(pages[7]))
            button8.place(x=0, y=500)
        elif (frame == "Housing") or (frame == "GraphsCraigs"):
            pages = pages + ["GraphsCraigs"]
            button8 = tk.Button(self.w, text="More Statistics", fg="#03717D", width=12, height=1,
                                command=lambda: self._go_to(pages[7]))
            button8.place(x=0, y=500)
    
    def _button(self):
        pages = ["StartPage", "Vaccine", "Demographics", "Weather", "Acts", "AllEvents", "Housing"]
        button1 = tk.Button(self.w, text="Main Menu", fg="#03717D", width=12, height=1,
                            command=lambda: self._go_to(pages[0]))
        button2 = tk.Button(self.w, text="Vaccination", fg="#03717D", width=12, height=1,
                            command=lambda: self._go_to(pages[1]))
        button3 = tk.Button(self.w, text="Demographics", fg="#03717D", width=12, height=1,
                            command=lambda: self._go_to(pages[2]))
        button4 = tk.Button(self.w, text="Weather", fg="#03717D", width=12, height=1,
                            command=lambda: self._go_to(pages[3]))
        button5 = tk.Button(self.w, text="Volunteering", fg="#03717D", width=12, height=1,
                            command=lambda: self._go_to(pages[4]))
        button6 = tk.Button(self.w, text="Events", fg="#03717D", width=12, height=1,
                            command=lambda: self._go_to(pages[5]))
        button7 = tk.Button(self.w, text="Housing", fg="#03717D", width=12, height=1,
                            command=lambda: self._go_to(pages[6]))
        button1.place(x=0, y=150)
        button2.place(x=0, y=200)
        button3.place(x=0, y=250)
        button4.place(x=0, y=300)
        button5.place(x=0, y=350)
        button6.place(x=0, y=400)
        button7.place(x=0, y=450)

    def _go_to(self, frame: str):
        self.controller.update_globals(frame)
        self.controller.show_frame(frame)
