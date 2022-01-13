import json

import pandas as pd
import requests

from scraper.scraper import Scraper


class AirVisualScraper(Scraper):
    def __init__(self, city, state, country):
        """Initialize Air visualizer
        Args:
            city (str): City to search.
            state (str): State city is located at.
            country (str): Country to search.
        """
        self.city = city
        self.state = state
        self.country = country
        self.key = "daab8f56-b1d2-40f7-b87b-44f8fac789d1"  # API KEY
        self.url = f"http://api.airvisual.com/v2/city?city={self.city}&state={self.state}&country={self.country}&key={self.key}"
        self.results = None

    def scrape(self):
        """Stores json request
           from the api in results
        """
        payload = {}
        headers = {}
        response = requests.request("GET", self.url, headers=headers, data=payload)
        self.results = json.loads(response.text)

    def get_df(self) -> pd.DataFrame:
        """Returns DataFrame with cleaned data

        Returns:
            DataFrame: with parsed results
        """
        df = pd.DataFrame()
        df = df.append(self.results["data"]["current"]["pollution"], index=[self.results["data"]["city"]])
        return df
