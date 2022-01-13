import tkinter as tk
import pandas as pd
from tkinter import font as tkfont
from frames.frame import Frame
from scraper import AllEventsScrapper
from utils import gen_map


class AllEvents(Frame):
    def __init__(self, parent, controller):
        """Handle integration into Tkinter parent app
        """
        super(AllEvents, self).__init__(parent, controller)
        self.city = ""
        self.results = ""
        self.df = None
        self.local = None
        self.searchlabel = tk.Label(self, text="What's Hot Here?",
                                    font=tkfont.Font(family='Helvetica', size=12, weight="bold"), fg="#03717D")
        self.searchlabel.place(x=208, y=60)

    def transition(self, address, local):
        """Displays elements of Housing
        Args:
            address (str): Full address.
            local (bool): boolean to check if local data must be used.
        """
        self._menu("AllEvents")
        city = address.split(",")[0]
        if self.city != city or self.local != local:
            self.local = local
            self.results = ""
            self.city = city
            if local:
                self.df = pd.read_csv("local/alleventsgoe.csv")
            else:
                events = AllEventsScrapper(self.city)
                events.scrape()
                self.df = events.get_df()
                self._graph(address)

            self._gen_table()

        label = tk.Text(self, width=149, fg="#03717D")
        label.insert(tk.END, self.results)
        label.place(x=208, y=100)

    def _graph(self, address: str):
        """ Create graphs with location of events
        """
        gen_map(self.df, address)

    def _gen_table(self):
        """ Creates table with information about the events
        """
        self.results += "\n"
        result = ' {Event:80}  {Date:30}  {Venue:30}'.format(Event="Event Name", Date="Date", Venue="Venue")
        self.results += result + "\n"
        result = ' {Event:80}  {Date:30}  {Venue:30}'.format(Event="-" * 80, Date="-" * 30, Venue="-" * 30)
        self.results += result + "\n"
        for index, row in self.df.iterrows():
            vals = row.to_dict()
            vals["Event Name"] = vals["Event Name"] if len(vals["Event Name"]) < 75 else vals["Event Name"][:75] + "..."
            vals["Date"] = vals["Date"][4:]
            vals["Venue"] = vals["Venue"] if len(vals["Venue"]) < 30 else vals["Venue"][:30] + "..."
            result = ' {Event Name:80}  {Date:30}  {Venue:30}'.format(**vals)
            self.results += result + "\n"
