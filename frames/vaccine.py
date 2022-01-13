import tkinter as tk
from datetime import datetime, timedelta

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from PIL import ImageTk, Image

from frames.frame import Frame
from scraper import CovidScraper


class Vaccine(Frame):
    def __init__(self, parent, controller):
        """Handle integration into Tkinter parent app
        """
        super(Vaccine, self).__init__(parent, controller)
        self.county = ""
        self.df = None
        self.local = None

    def transition(self, address, local):
        """Displays elements of Vaccine
        Args:
            address (str): Full address.
            local (bool): boolean to check if local data must be used.
        """
        self._menu("Vaccine")
        if address.count(",") == 3:
            county = address.split(",")[1].strip()
        else:
            county = address.split(",")[0].strip()

        if "County" not in county:
            county += " County"

        if self.county != county or self.local != local:
            self.local = local
            self.county = county
            if local:
                self.df = pd.read_csv('local/vaccine.csv')
            else:
                vaccine = CovidScraper()
                vaccine.scrape()
                self.df = vaccine.get_df()
                self._graph()

        if local:
            im = Image.open("local/firstvaccine.png")
        else:
            im = Image.open("tmp/firstvaccine.png")
        photo = ImageTk.PhotoImage(im)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=327, y=80)

    def _graph(self):
        """ Create graph for vaccination level
        """
        df1 = self.df.loc[self.df['Recip_County'] == self.county].copy()
        df1['date'] = pd.to_datetime(self.df['Date'])
        N_DAYS_AGO = 10
        today = datetime.now()
        n_days_ago = today - timedelta(days=N_DAYS_AGO)
        df1 = df1[df1.date >= n_days_ago]
        fig, axes = plt.subplots(2, 1, figsize=(15, 10))
        sns.set(font_scale = .5)
        a = sns.lineplot(data=df1.iloc[::-1], x="Date", y="Series_Complete_Yes", ax=axes[0])
        a.set(xlabel="Date", ylabel="Number of People")
        a.set_title("People Vaccinated with First Dose in Last 10 Days", fontsize=10)
        b = sns.lineplot(data=df1.iloc[::-1], x="Date", y="Administered_Dose1_Recip", ax=axes[1])
        b.set(xlabel="Date", ylabel="Number of People")
        b.set_title("People Vaccinated with Both Doses in Last 10 Days", fontsize=10)
        fig.set_size_inches(8, 6)
        fig.tight_layout(pad=1.0)
        plt.savefig("tmp/firstvaccine.png", dpi=100)
