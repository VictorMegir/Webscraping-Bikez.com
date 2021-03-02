# Webscraping Bikez.com

Web scraping the Bikez.com website to create a dataset of 38.000 bike models.

### Bikez.com

<a href='https://bikez.com/main/index.php'>Bizez.com</a> is a website that features an extensive list of bike models old and new.<br>
For each bike this website features a variety of stats and details about different aspects and attributes of the bike.

### Tools

To extract the data I used the Python programming language as well as some of its modules.
* For requests I used the <a href='https://requests.readthedocs.io/en/master/'>Requests</a> module.
* For the web scraping I used the <a href='https://www.crummy.com/software/BeautifulSoup/bs4/doc/'>Beautiful Soup</a> module
* For cleaning and transforming the data I used the <a href='https://pandas.pydata.org/'>Pandas</a> module.
* To save the raw data I used a json file. To save the cleaner data I used a csv file.

### Data
Each model is uniquely defined by the model name as well as the year of release.
The same model can be relased in multiple years, thus several model names may appear multiple times.<br>
There are several columns of the data that I wasn't able to clean due to a lack of knowledge on bikes.<br>
For many columns where I expected to get a few distinct string values, I was med instead with a variety of string values with major inconsitencies that were difficult and time consumming to standardize. Given how most of the entries had missing values for these columns, I decided to not go through the trouble cleaning them.
