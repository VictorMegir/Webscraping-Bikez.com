import urllib.request

print('Downloading url collection...')

url = 'https://raw.githubusercontent.com/VictorMegir/Webscraping-Bikez.com/master/models.csv'
urllib.request.urlretrieve(url, 'urls.csv')

print('Download Complete.')
