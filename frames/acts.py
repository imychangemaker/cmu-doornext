import tkinter as tk
import pandas as pd
from frames.frame import Frame
from scraper import CreateTheGoodScraper


class Acts(Frame):
    def __init__(self, parent, controller):
        super(Acts, self).__init__(parent, controller)
        self.local = ""
        self.city = ""
        self.df = None
        self.results = None

    def transition(self, address, local):
        """Displays elements of Weather
        Args:
            address (str): Not used.
            local (bool): boolean to check if local data must be used.
        """
        self._menu("Acts")
        if self.city != address or self.local != local:
            self.city = address
            self.local = local
            if local:
                self.df = pd.read_csv("local/Eventslocal.csv")
            else:
                acts = CreateTheGoodScraper("driver/chromedriver")
                acts.scrape(address)
                self.df = acts.get_df()

            self.results = ""
            self._gen_table()

        label = tk.Text(self, width=149, fg="#03717D")
        label.insert(tk.END, self.results)
        label.place(x=208, y=80)

    def _gen_table(self):
        """ Creates table with information about events
        """
        self.results += "\n"
        result = ' {Event:40}  {Description:70}  {Status:30}'.format(Event="Volunteer Event", Description="Description",
                                                                     Status="Status")
        self.results += result + "\n"
        result = ' {Event:40}  {Description:70}  {Status:30}'.format(Event="-" * 40, Description="-" * 70,
                                                                     Status="-" * 30)
        self.results += result + "\n"
        for index, row in self.df.iterrows():
            vals = row.to_dict()
            vals["title"] = vals["title"] if len(vals["title"]) < 35 else vals["title"][:35] + "..."
            vals["desc"] = vals["desc"] if len(vals["desc"]) < 65 else vals["desc"][:65] + "..."
            vals["where"] = vals['where'].replace("\n", " ")
            result = '{title:40}  {desc:70}  {where:30}'.format(**vals)
            self.results += " " + result + "\n"
