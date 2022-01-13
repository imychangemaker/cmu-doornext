import pandas as pd
import requests
from bs4 import BeautifulSoup

from scraper.scraper import Scraper


class TimeAndDateScraper(Scraper):
    def __init__(self, city, country):
        """Initialize Time and Date
        Args:
            city (str): City to search.
            country (str): Country.
        """
        self.city = city
        self.country = country
        self.results = None

    def scrape(self):
        """Searches in timeanddate for data matching the city and country
           stores it in results
        """
        url = f'https://www.timeanddate.com/weather/{self.country}/{self.city}'
        response = requests.get(url)
        html_doc = response.content
        soup = BeautifulSoup(html_doc, 'html.parser')
        self.results = soup.find_all("section", {"class": "bk-focus"})

    def get_df(self) -> pd.DataFrame:
        """Parses the raw bs4 results into a dataframe and retunrs it

        Returns:
            DataFrame: with parsed results
        """
        d = {}
        words = self.results[0].find("div", {"class": "bk-focus__info"}).find_all("td")
        strings3 = self.results[0].find("div", {"class": "bk-focus__qlook"}).find(
            "p").next_sibling.next_sibling.text.split('°F')
        d['Temperature'] = self.results[0].find("div", {"class": "bk-focus__qlook"}).find("div",
                                                                                          {"class": "h2"}).text.replace(
            u'\xa0', u'')
        d['Forecast'] = self.results[0].find("div", {"class": "bk-focus__qlook"}).find("span", {
            "title": "High and low forecasted temperature today"}).text.replace(u'\xa0', u'')
        d['Feels Like'] = strings3[0]
        d['Forecast'] = strings3[1]
        d['Wind'] = strings3[2]
        d['Location'] = words[0].text
        d['Time'] = words[1].text
        d['Visibility'] = words[3].text
        d['Pressure'] = words[4].text
        d['Humidity'] = words[5].text
        d['Dew'] = words[6].text
        df = pd.DataFrame(d, index=[0])
        return df
