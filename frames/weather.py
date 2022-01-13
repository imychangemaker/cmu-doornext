import tkinter as tk

import pandas as pd

from frames.frame import Frame
from scraper import TimeAndDateScraper


class Weather(Frame):
    def __init__(self, parent, controller):
        """Handle integration into Tkinter parent app
         """
        super(Weather, self).__init__(parent, controller)
        self.city = ""
        self.results = ""
        self.df = None
        self.local = None

    def transition(self, address, local):
        """Displays elements of Weather
        Args:
            address (str): Full address.
            local (bool): boolean to check if local data must be used.
        """
        city = address.split(",")[0]
        self._menu("Weather")
        if self.city != city or self.local != local:
            self.local = local
            self.results = ""
            self.city = city
            if local:
                self.df = pd.read_csv("local/Weatherlocal.csv")
            else:
                weather = TimeAndDateScraper(self.city.replace(" ", ""), "usa")
                weather.scrape()
                self.df = weather.get_df()
            self._gen_table()

        label = tk.Text(self, width=125, fg="#03717D")
        label.insert(tk.END, self.results)
        label.place(x=293, y=80)

    def _gen_table(self):
        """ Creates table with information about events
        """
        for index, row in self.df.iterrows():
            vals = row.to_dict()
            for k, v in vals.items():
                if k != "Unnamed: 0":
                    interpretation = self._interpret(k, v)
                    self.results += "\n"
                    result = '{Index:14}{Values:40}{Interpretation:100}'.format(Index=k,
                                                                        Values=v,
                                                                        Interpretation=interpretation)
                    self.results += " " + result

    def _interpret(self, k, v):
        """Maps functions to values and returns interpretation
        Args:
            vals (str): Dictionary of df row with columns 'Unnamed: 0' and 'Values'.

        Returns:
            interpretation
        """

        dictionary = {"Temperature": self._temp,
                      "Forecast": self._forecast,
                      "Location": self._location,
                      "Visibility": self._visibility,
                      "Pressure": self._pressure,
                      "Humidity": self._humidity}
        try:
            index_function = dictionary[k]
            interpretation = index_function(v)
        except KeyError:
            interpretation = ' '

        return interpretation

    def _humidity(self, value):
        """Interprets dew point
        Args:
            value (str): Values column of df.

        Returns:
            interpretation
        """
        value = float(value.split("%")[0])
        if value >= 65:
            return "Lots of moisture in the air, very uncomfortable"
        elif (value >= 55) and (value < 65):
            return "Sticky weather with muggy evenings"
        elif value < 55:
            return "Dry and comfortable weather"
        else:
            return "NA"

    def _pressure(self, value):
        """Interprets pressure
        Args:
            value (str): Values column of df.

        Returns:
            interpretation
        """
        value = float(value[:5])
        if value >= 30.20:
            return "High pressure is associated with clear skies"
        elif (value >= 29.80) and (value < 30.20):
            return "Normal pressure is associated with steady weather"
        elif value < 29.80:
            return "Low pressure is associated with warm air and rainstorms"
        else:
            return "NA"

    def _visibility(self, value):
        """Interprets air quality
        Args:
            value (str): Values column of df.

        Returns:
            interpretation
        """
        value = int(value[:2])
        if value >= 10:
            return "Excellent visibility"
        elif value >= 6 and value < 10:
            return "Good visibility"
        elif value >= 3 and value <= 5:
            return "visible"
        elif value >= 1.5 and value <= 2.75:
            return "Short visibility"
        elif value >= 1 and value <= 1.25:
            return "Really shor visibility "
        elif value < 1.25:
            return "Almost no visibility"
        else:
            return "NA"

    def _temp(self, value):
        """Interprets temperature
        Args:
            value (str): Values column of df.

        Returns:
            interpretation
        """
        value = int(value.split("°")[0])
        if value <= 118 and value > 106:
            return "Extremely hot weather"
        elif value <= 106 and value > 87:
            return "It is very hot"
        elif value <= 87 and value > 77:
            return "It is hot"
        elif value <= 77 and value > 66:
            return "It is warm"
        elif value <= 66 and value > 56:
            return "It is fresh"
        elif value <= 56 and value > 40:
            return "It is cold"
        else:
            return "It is too cold"

    def _forecast(self, value):
        """Interprets forecast
        Args:
            value (str): Values column of df.

        Returns:
            interpretation
        """
        value = value[10:]
        return "Max/Min expected temperature for today"

    def _location(self, value):
        """Interprets location
        Args:
            value (str): Values column of df.

        Returns:
            interpretation
        """
        return "Information was retrieved from this specific location"

