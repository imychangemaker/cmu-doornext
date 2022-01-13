import tkinter as tk
import matplotlib.pyplot as plt
import pandas as pd
from PIL import ImageTk, Image
from frames.frame import Frame
from scraper import DemographicsScrapper


class Demographics(Frame):
    def __init__(self, parent, controller):
        """Handle integration into Tkinter parent app
        """
        super(Demographics, self).__init__(parent, controller)
        self.city = ""
        self.state = ""
        self.df = None
        self.df2 = None
        self.local = None

    def transition(self, address: str, local: bool):
        """Displays elements of Demographics
        Args:
            address (str): Full address.
            local (bool): boolean to check if local data must be used.
        """
        self._menu("Demographics")
        city = address.split(",")[0]
        state = address.split(',')[-2].strip()
        if self.city != city or self.local != local:  # Check if city changed if not continue displaying the same data
            self.local = local
            self.city = city
            self.state = state
            if local:  # If set to local use local data
                self.df = pd.read_csv("local/demographics1.csv")
                self.df2 = pd.read_csv("local/demographics2.csv")
            else:
                demographics = DemographicsScrapper()
                demographics.scrape()
                self.df2, self.df = demographics.get_df()
                self._graph()

        if local:
            im = Image.open("local/demographics.png")
        else:
            im = Image.open("tmp/demographics.png")
        photo = ImageTk.PhotoImage(im)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=327, y=80)

    def _graph(self):
        """ Create graph of demographics
        """
        df1 = self.df.loc[self.df['City'] == self.city].copy()
        df3 = self.df2.loc[self.df2['State'] == self.state].copy()

        fig, axes = plt.subplots(2, 1, figsize=(15, 10))
        df3.plot(y=['Republican', 'None', 'Democrats'], kind="bar", ax=axes[0], title="Party Affiliation",
                 xlabel="Party", ylabel="Number of Adults")
        df1.plot(y=["Robbery", 'Murder andNonnegligentmanslaughter', 'Rape1', 'Robbery',
                    'Aggravatedassault', 'Burglary', 'Larceny-theft',
                    'Motorvehicletheft', 'Arson2'], kind="bar", ax=axes[1], title="Cities by Crime Rate",
                 xlabel="Type of Crime", ylabel="Crime Rates")
        plt.legend(["Murder", "Rape", "Robbery", "Assault", "Burglary", "Theft", "Motor Theft", "Arson"])
        fig.set_size_inches(8, 6)
        fig.tight_layout(pad=1.0)
        plt.savefig("tmp/demographics.png", dpi=100)
