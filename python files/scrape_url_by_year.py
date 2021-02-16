from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime
from scrape_urls import scrape_year

urls = pd.read_csv('urls.csv')

def update_by_year(year=datetime.datetime.now().year):
    year_url = 'https://bikez.com/year/'+ str(year) + '-motorcycle-models.php'
    year_models = scrape_year(year_url)
    year_models['Year'] = int(year)
    return year_models

urls = pd.concat([update_by_year(), urls])
urls.reset_index()
urls.to_csv('urls.csv', index=False)
