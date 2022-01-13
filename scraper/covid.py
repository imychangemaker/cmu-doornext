import pandas as pd

from scraper.scraper import Scraper


class CovidScraper(Scraper):
    def __init__(self):
        self.results = None

    def scrape(self):
        """Scrapes data from cdc
        """
        self.results = pd.read_csv("https://data.cdc.gov/api/views/8xkx-amqh/rows.csv?accessType=DOWNLOAD",
                                   low_memory=False)

    def get_df(self) -> pd.DataFrame:
        """Returns data from cdc in DataFrame
        """
        return self.results
