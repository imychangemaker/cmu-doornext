import time

import pandas as pd
import requests
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CreateTheGoodScraper():
    def __init__(self, driver_path: str):
        """Initialize Demographics
           Args:
                driver_path (str): Path to chromedriver
        """
        self.driver_path = driver_path
        self.results = None

    def _get_driver(self):
        """Initialize the scraper and sets options for
           headless scrapping
        """
        driver_path = self.driver_path
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = Chrome(executable_path=driver_path, options=chrome_options)
        return driver

    def _click_by_xpath(self, xpath, driver):
        """Select an element
        """
        return WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.XPATH, xpath)))

    def _select_by_xpath(self, xpath, zipcode, driver):
        """Send keys to selected element
        """
        time.sleep(1)
        text_field = self._click_by_xpath(xpath, driver)
        text_field.click()
        for i in range(5):
            text_field.send_keys(Keys.BACKSPACE)
        text_field.send_keys(zipcode)

    def scrape(self, address):
        """Retrieves data from Create The Good and stores it in
           variable results.
        """
        url = 'https://nominatim.openstreetmap.org/search/'
        params_dict = {'q': f"subway {address}", 'format': 'json'}  # since its the store with most locations
        r = requests.get(url, params=params_dict)
        zipcode = r.json()[0]['display_name'].split(",")[-2].strip()
        driver = self._get_driver()
        driver.get('https://createthegood.aarp.org/volunteer-search/')
        self._select_by_xpath(
            "/html/body/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div[2]/input", zipcode,
            driver)
        self._click_by_xpath(
            "/html/body/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div[4]/button",
            driver).click()
        time.sleep(1)
        li = []
        try:
            for i in range(1, 20):
                tmp = {}
                tmp['title'] = driver.find_element_by_xpath(
                    f'//*[@id="aarp-c-body"]/div/div/div[2]/div/div/div/div/div/div/div/div/div[3]/div/div[2]/div[{i}]/div[1]/h4').text
                tmp['desc'] = driver.find_element_by_xpath(
                    f'//*[@id="aarp-c-body"]/div/div/div[2]/div/div/div/div/div/div/div/div/div[3]/div/div[2]/div[{i}]/div[1]/p').text
                tmp['where'] = driver.find_element_by_xpath(
                    f'//*[@id="aarp-c-body"]/div/div/div[2]/div/div/div/div/div/div/div/div/div[3]/div/div[2]/div[{i}]/div[2]/div[2]/div[1]').text
                tmp['where'] = driver.find_element_by_xpath(
                    f'//*[@id="aarp-c-body"]/div/div/div[2]/div/div/div/div/div/div/div/div/div[3]/div/div[2]/div[{i}]/div[2]/div[1]/div/div[2]').text
                li.append(tmp)
        except:
            pass
        driver.quit()
        self.results = li

    def get_df(self) -> pd.DataFrame:
        """Returns DataFrame with cleaned data

        Returns:
            DataFrame: with parsed results
        """
        df = pd.DataFrame.from_dict(self.results)
        return df
