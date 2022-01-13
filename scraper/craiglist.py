import pandas as pd
import requests
from bs4 import BeautifulSoup

from scraper.scraper import Scraper


class CraigListScraper(Scraper):
    def __init__(self, city: str, query: str):
        """Initialize Craig List
        Args:
            city (str): City to search.
            query (str): Kind of object to search for.
        """
        self.city = city
        self.query = query
        self.results = None

    def scrape(self):
        """Searches in Craigslist for results matching the city and query provided
           stores them in the instance variable results.
        """
        url = f'https://{self.city}.craigslist.org/d/housing/search/hhh?query={self.query}&sort=rel'
        response = requests.get(url)
        html_doc = response.content
        soup = BeautifulSoup(html_doc, 'html.parser')
        self.results = soup.find_all("div", {"class": "result-info"})

    def get_df(self) -> pd.DataFrame:
        """Parses the raw bs4 results into a dataframe and retunrs it

        Returns:
            DataFrame: with parsed results
        """
        li = []
        for result in self.results:
            try:
                d = {}
                d['Name'] = result.find("a", {"class": "result-title hdrlnk"}).text
                d['Price'] = result.find("span", {"class": "result-price"}).text
                d['Detail'] = " ".join(
                    result.find("span", {"class": "housing"}).text.replace("\n", "").replace("-", "").split()) if (
                    result.find("span", {"class": "housing"})) else " "
                li.append(d)
            # handle empty results.
            except:
                pass

        df = pd.DataFrame.from_dict(li)
        # Clean and change data type of extra columns.
        df["Rooms"] = df['Detail'].str.extract(r'([0-9]br)')[0].str[0].fillna(0).astype(int)
        df["Size"] = df['Detail'].str.extract(r'([0-9]+ft)')[0].str[:-2].fillna(0).astype(int)
        df["Price"] = df["Price"].str[1:].str.replace(",", "").astype(float)
        return df
