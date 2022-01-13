import tkinter as tk
from tkinter import font as tkfont

import requests

from frames import Acts, AllEvents, GraphsCraigs, Demographics, Housing, Map, StartPage, Vaccine, Weather


class MyGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.title("DoorNext")
        self.geometry('1280x720')
        self.bind("<F11>", self.toggle_fullscreen)
        self.bind("<Escape>", self.end_fullscreen)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, AllEvents, Map, Housing, GraphsCraigs, Demographics, Vaccine, Weather, Acts):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.attributes("-fullscreen", False)
        return "break"
    
    def get_city(self):
        frame_main = self.frames["StartPage"]
        url = 'https://nominatim.openstreetmap.org/search/'
        params_dict = {'q': f"{frame_main.e_city.get()}", 'format': 'json'}
        r = requests.get(url, params=params_dict)
        city = r.json()[0]['display_name']
        return city
    
    def get_status(self):
        frame_main = self.frames["StartPage"]
        return frame_main.is_on
    
    def set_city(self, value):
        frame_main = self.frames["StartPage"]
        frame_main.e_city.delete(0, "end")
        frame_main.e_city.insert(0, value)
    
    def update_globals(self, frame):
        frame_main = self.frames["StartPage"]
        frame = self.frames[frame]
        if frame_main.is_on != True:
            url = 'https://nominatim.openstreetmap.org/search/'
            params_dict = {'q': f"{frame_main.e_city.get()}", 'format': 'json'}
            r = requests.get(url, params=params_dict)
            frame.transition(r.json()[0]['display_name'], False)
        else:
            frame.transition("Pittsburgh, Allegheny County, Pennsylvania, United States", True)


if __name__ == '__main__':
    app = MyGUI()
    app.mainloop()
