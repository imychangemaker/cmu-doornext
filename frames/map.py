import tkinter as tk

from PIL import ImageTk, Image

from frames.frame import Frame


class Map(Frame):
    def __init__(self, parent, controller):
        """Handle integration into Tkinter parent app
        """
        super(Map, self).__init__(parent, controller)

    def transition(self, _, local):
        """Displays elements of Housing
        Args:
            _ (str): Not used.
            local (bool): boolean to check if local data must be used.
        """
        self._menu("Map")
        if local:
            im = Image.open("local/map.png")
        else:
            im = Image.open("tmp/map.png")
        photo = ImageTk.PhotoImage(im)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=327, y=80)
