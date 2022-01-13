import tkinter as tk
import matplotlib.pyplot as plt
import pandas as pd
from tkinter import font as tkfont
from frames.frame import Frame
from scraper import CraigListScraper


class Housing(Frame):
    def __init__(self, parent, controller):
        """Handle integration into Tkinter parent app
        """
        super(Housing, self).__init__(parent, controller)
        self.city = ""
        self.results = ""
        self.df = None
        self.local = None
        self.searchlabel = tk.Label(self, text="Find Yourself a Comfy Home",
                                    font=tkfont.Font(family='Helvetica', size=12, weight="bold"), fg="#03717D")
        self.searchlabel.place(x=208, y=60)

    def transition(self, address, local):
        """Displays elements of Housing
        Args:
            address (str): Full address.
            local (bool): boolean to check if local data must be used.
        """
        self._menu("Housing")
        city = address.split(",")[0]
        if self.city != city or self.local != local:
            self.local = local
            self.results = ""
            self.city = city.replace(" ", "")
            if local:
                self.df = pd.read_csv("local/craigs.csv")
            else:
                events = CraigListScraper(self.city, "Apartments")
                events.scrape()
                self.df = events.get_df()

            self._gen_table()

        label = tk.Text(self, width=149, fg="#03717D")
        label.insert(tk.END, self.results)
        label.place(x=208, y=100)

    def _graph(self):
        """ Create graphs about Craigslist housing options
        """
        fig, axes = plt.subplots(2, 2)
        self.df[self.df["Rooms"] > 0]["Rooms"].value_counts().plot.bar(title="Number of Rooms", ax=axes[0, 0])
        self.df[self.df["Size"] > 0].sort_values("Price").plot.scatter(x="Price", y="Size",
                                                                       title="Price x Size Relation",
                                                                       ax=axes[0, 1])
        self.df[self.df["Size"] > 0].sort_values("Size").plot.line(x="Size", y="Rooms", title="Rooms by Size",
                                                                   ax=axes[1, 0])
        self.df[self.df["Size"] > 0].sort_values("Price").plot.line(x="Price", y="Rooms",
                                                                    title="Rooms by Price", ax=axes[1, 1])
        fig.tight_layout(pad=1.0)
        plt.savefig("tmp/craig.png", dpi=100)

    def _gen_table(self):
        """ Creates table with information about the listings
        """
        self.results += "\n"
        result = ' {Name:80}  {Price:20}  {Detail:20}'.format(Name="Listing", Price="Price", Detail="Details")
        self.results += result + "\n"
        result = ' {Name:80}  {Price:20}  {Detail:20}'.format(Name="-" * 80, Price="-" * 20, Detail="-" * 20)
        self.results += result + "\n"
        for index, row in self.df.iterrows():
            vals = row.to_dict()
            vals["Name"] = vals["Name"] if len(vals["Name"]) < 75 else vals["Name"][:75] + "..."
            vals["Price"] = vals["Price"]
            vals["Detail"] = vals["Detail"]
            result = ' {Name:80}  {Price:<20}  {Detail:20}'.format(**vals)
            self.results += result + "\n"
