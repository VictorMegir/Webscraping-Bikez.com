from bs4 import BeautifulSoup
import requests
import pandas as pd

models = pd.DataFrame(columns=['Model', 'Year', 'URL'])

starting_url = 'https://bikez.com/years/index.php'
starting_request = requests.get(starting_url)
starting_soup = BeautifulSoup(starting_request.text, 'html.parser')

def scrape_year(year_url):
    year_request = requests.get(year_url)
    year_soup = BeautifulSoup(year_request.text, 'html.parser')
    
    even_entries = year_soup.findAll('tr', ({'class': 'even'}))
    odd_entries = year_soup.findAll('tr', ({'class': 'odd'}))
    all_entries = even_entries + odd_entries
    
    year_models = pd.DataFrame(columns=['Model', 'Year', 'URL'])
    index = 0
    
    for entry in all_entries:
        if len(entry) == 1:
            model = entry.td.a.text
            if model =='': continue
            url = 'https://bikez.com' + entry.td.a['href'].split('..')[1]
        if len(entry) == 2:
            last_td = entry.findAll('td')[-1]
            if last_td.has_attr('colspan'):
                model = last_td.a.text
                if model =='': continue
                url = 'https://bikez.com' + last_td.a['href'].split('..')[1]
        if len(entry) == 3:
            model = entry.td.a.text
            if model =='': continue
            url = 'https://bikez.com' + entry.td.a['href'].split('..')[1]

        year_models.loc[index] =[model, 0, url]
        index += 1
    return year_models

def scrape_all_years():
    even_years = starting_soup.findAll('td', {'class': 'even'})
    odd_years = starting_soup.findAll('td', {'class': 'odd'})
    all_years = even_years + odd_years
    global models
    
    for year in all_years:
        year_url = 'https://bikez.com' + year.a['href'].split('..')[1]
        year_models = scrape_year(year_url)
        year_models['Year'] = int(year.a.text)
        models = models.append(year_models)

    models.to_csv('models.csv', index=False)
    return
