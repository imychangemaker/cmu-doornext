import pandas as pd
import requests
from bs4 import BeautifulSoup

from scraper.scraper import Scraper


class AllEventsScrapper(Scraper):
    def __init__(self, city: str):
        """Initialize Allevent
        Args:
            city (str): City to search.
        """
        self.city = city

    def scrape(self):
        """Searches in allevents.in for data matching the city
           stores it in results
        """
        url = f'https://allevents.in/{self.city}'
        response = requests.get(url)
        html_doc = response.content
        soup = BeautifulSoup(html_doc, 'html.parser')
        self.results = soup.find_all("li", {"class": "item"})

    def get_df(self) -> pd.DataFrame:
        """Parses the raw bs4 results into a dataframe and retunrs it

        Returns:
            DataFrame: with parsed results
        """
        li = []
        for result in self.results:
            if not (result.find("span", {"class": "up-venue toh"}).text.strip() == 'Online'):
                d = {}
                d['Event Name'] = result.find("div", {"class": "title"}).text.strip()
                d['Date'] = result.find("span", {"class": "up-time-display"}).text.strip() if (
                    result.find("span", {"class": "up-time-display"})) else " "
                d['Venue'] = result.find("span", {"class": "up-venue toh"}).text.strip() if (
                    result.find("span", {"class": "up-venue toh"})) else " "
                li.append(d)
        df = pd.DataFrame.from_dict(li)
        return df
