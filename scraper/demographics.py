import pandas as pd

from scraper.scraper import Scraper


class DemographicsScrapper(Scraper):
    def __init__(self):
        """Initialize Demographics
        """
        self.results_crime = None
        self.results_politician = None

    def scrape(self):
        """Searches in Wikipedia and retrieves data about
           crimes and political views.
        """
        self.results_crime = pd.read_html("https://en.wikipedia.org/wiki/List_of_United_States_cities_by_crime_rate")[0]
        self.results_politician = \
        pd.read_html("https://www.pewforum.org/religious-landscape-study/compare/party-affiliation/by/state/")[0]

    def _clean_crime_rate_df(self):
        """Helper function to change the headers"""
        headers = ['State', 'City', 'Population', 'Total', 'Murder andNonnegligentmanslaughter', 'Rape1', 'Robbery',
                   'Aggravatedassault', 'Total', 'Burglary', 'Larceny-theft', 'Motorvehicletheft', 'Arson2']
        self.results_crime.columns = headers

    def _clean_politician_df(self):
        """Helper function clean the dataframe"""
        df = self.results_politician.loc[:50].copy()
        df['Republican/lean Rep.'] = df['Republican/lean Rep.'].str.strip('%').astype(int)
        df['No lean'] = df['No lean'].str.strip('%').astype(int)
        df['Democrat/lean Dem.'] = df['Democrat/lean Dem.'].str.strip('%').astype(int)
        df['Sample Size'] = df['Sample Size'].astype(int)
        df['Republican'] = df['Republican/lean Rep.'] * df['Sample Size'] / 100
        df['None'] = df['No lean'] * df['Sample Size'] / 100
        df['Democrats'] = df['Democrat/lean Dem.'] * df['Sample Size'] / 100
        self.results_politician = df

    def get_df(self) -> pd.DataFrame:
        """Returns DataFrame with cleaned data

        Returns:
            DataFrame: with parsed results
        """
        self._clean_politician_df()
        self._clean_crime_rate_df()
        return self.results_politician, self.results_crime
