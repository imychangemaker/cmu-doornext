import tkinter as tk

from PIL import ImageTk, Image

from frames.frame import Frame


class GraphsCraigs(Frame):
    def __init__(self, parent, controller):
        super(GraphsCraigs, self).__init__(parent, controller)

    def transition(self, _, local):
        """Displays elements of Housing
        Args:
            _ (str): Not used.
            local (bool): boolean to check if local data must be used.
        """
        self._menu("GraphsCraigs")
        if local:
            im = Image.open("local/craig.png")
        else:
            im = Image.open("tmp/craig.png")
        photo = ImageTk.PhotoImage(im.resize((800, 600)))
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=327, y=80)