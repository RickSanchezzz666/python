from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
driver = webdriver.Chrome()

driver.get('https://varta1.com.ua/archive/')
time.sleep(1)

df = pd.DataFrame({'Date': [], 'Text': []})

def update_df(date, text):
    df.loc[len(df)] = {'Date': date, 'Text': f'{text}'}
    df.to_csv('archives.csv', index=False)

dates_to_visit = []

dates = []

format_link = lambda year, month, day: f'https://varta1.com.ua/archive/{year}-{month}-{day}/'

def get_data(date_to_visit, date):
    try:
            articles = []
            driver.get(date_to_visit)

            articles = driver.find_elements(By.CSS_SELECTOR, "article.post > a[href]")

            for article in articles:
                try:
                    href = article.get_attribute('href')
                    driver.get(href)
                    main = driver.find_elements(By.CSS_SELECTOR, "main p")
                    text = [p.text for p in main]
                    driver.back()
                    update_df(date, text)
                except StaleElementReferenceException:
                    pass
    except NoSuchElementException:
        pass

for year in [2019, 2020, 2021, 2022, 2023]:
    for month in [6]:
        for day in [13]:
            dates_to_visit.append(format_link(year, month, day))
            dates.append(f'{year}-{month}-{day}')

for i in range(len(dates_to_visit)):
    get_data(dates_to_visit[i], dates[i])

time.sleep(10)

input('Нажми шось: ')