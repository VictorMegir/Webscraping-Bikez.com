import urllib.request

print('Downloading url collection...')

url = 'https://raw.githubusercontent.com/VictorMegir/Webscraping-Bikez.com/master/models.csv?token=AGEM6LUWIENI6L4XRHMQMM3AFQWXI'
urllib.request.urlretrieve(url, 'urls.csv')

print('Download Complete.')
