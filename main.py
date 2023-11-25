from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import requests

driver = webdriver.Chrome()

driver.get('https://varta1.com.ua/archive/')
time.sleep(2)

df = pd.DataFrame({'Date': [], 'Text': []})

def update_df(date, text):
    df.loc[len(df)] = {'Date': date, 'Text': f'{text}'}
    df.to_csv('archives.csv', index=False)

dates_to_visit = []

try:
    dates_to_visit = driver.find_elements(By.XPATH, '//a[contains(@href, "/archive/")]')
    for date in dates_to_visit:
        try:
            parent_div = date.find_element(By.XPATH, './ancestor::div[contains(@class, "days")]')
        except NoSuchElementException:
            dates_to_visit.remove(date)
except NoSuchElementException:
    pass

date_hrefs = [date.get_attribute('href') for date in dates_to_visit]

try:
    for date_href in date_hrefs:
        articles = []
        time.sleep(1)
        driver.get(date_href)
        time.sleep(2.5)
        articles = driver.find_elements(By.XPATH, './/a[contains(@href, "/news/")]')

        dates = driver.find_elements(By.XPATH, './/time[contains(@datetime, "2023")]')

        time_text = dates[1].text

        for article in articles:
            try:
                href = article.get_attribute('href')
                response = requests.get(href)
                time.sleep(1)
                if (response.status_code == 200):
                    html = response.content
                    soup = BeautifulSoup(html, 'html.parser')
                    main_p_tags = soup.select('main[data-inited="1"] p')
                    text = [tag.get_text() for tag in main_p_tags]
                    update_df(time_text, text)
            except StaleElementReferenceException:
                pass
except NoSuchElementException:
    pass

time.sleep(10)

input('Нажми шось: ')