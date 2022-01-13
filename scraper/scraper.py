from abc import ABC, abstractmethod


class Scraper(ABC):
    @abstractmethod
    def scrape(self):
        """Abstract method to get data from the internet"""
        pass

    @abstractmethod
    def get_df(self):
        """Abstract method to clean data"""
        pass


