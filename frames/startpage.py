import threading
import tkinter as tk
from tkinter import font as tkfont

import cv2
from PIL import ImageTk, Image
from frames.frame import Frame


class StartPage(Frame):
    def __init__(self, parent, controller):
        super(StartPage, self).__init__(parent, controller)

        # Show header
        im = Image.open("pics/neighbourhood.jpg")
        photo = ImageTk.PhotoImage(im)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=208, y=0)

        self._menu("StartPage")
        
        # Entry for city information
        self.searchlabel = tk.Label(self, text="Start your search by zip code or area name",
                                    font=tkfont.Font(family='Helvetica', size=15, weight="bold"), fg="#03717D")
        self.searchlabel.place(x=230, y=390)
        self.e_city = tk.Entry(self, width=30, fg="grey", borderwidth=5)
        self.e_city.insert(0, "Pittsburgh")
        self.e_city.place(x=230, y=430)
        self.city = self.e_city.get()

        # Display on and off labels
        self.copylabel = tk.Label(self, text="Local data is only available for Pittsburgh.\nToggle OFF for non-Pittsburgh area.", font=tkfont.Font(family='Helvetica', size=12),
                                  fg="grey", anchor="e", justify="left")
        self.copylabel.place(x=230, y=480)
        self.is_on = True
        self.on = ImageTk.PhotoImage(Image.open("pics/on.png"))
        self.off = ImageTk.PhotoImage(Image.open("pics/off.png"))
        self.local = tk.Button(self, image=self.on, highlightthickness=0, bd=0, borderwidth=0, command=self.switch)
        self.local.place(x=232, y=530)
        
        # Search button
        button1 = tk.Button(self, text="Search", fg="#03717D",
                            command=lambda: self._go_to("Vaccine"))
        button1.place(x=226, y=630)

        # Display video
        self.label = tk.Label(self)
        self.label.place(x=618, y=345)
        video_source = "pics/Pitts.mp4"
        thread = threading.Thread(target=self.stream, args=(self.label, video_source))
        thread.daemon = 1
        thread.start()
    
    def transition(self, address, local):
        # Display menu options
        self._menu("StartPage")
        
    def go_to(self, frame):
        """ Transitions to frames
        """
        self.controller.update_globals(frame)
        self.controller.show_frame(frame)

    def stream(self, label, video_source):
        """ Stream video to label
        Args:
            label (tk.Label): Label where video should be streamed.
            video_source (path): path to video.
        """
        if True:
            cap = cv2.VideoCapture(video_source)
            count = 0
            while True:
                ret, frame = cap.read()
                count += 1
                if ret:
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
                    frame_image = ImageTk.PhotoImage(image = Image.fromarray(frame))
                    label.config(image=frame_image)
                    label.image = frame_image
                if count == cap.get(cv2.CAP_PROP_FRAME_COUNT):
                    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    count = 0
                    
    def switch(self):
        """ Sets is_on depending on event
        """
        if self.is_on:
            self.local.config(image=self.off)
            self.is_on = False
        else:
            self.local.config(image=self.on)
            self.is_on = True