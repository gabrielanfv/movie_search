import requests
from bs4 import BeautifulSoup

URL = "https://www.imdb.com/chart/top/?sort=us,desc&mode=simple&page=1"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

table = soup.find('tbody', attrs = {'class':'lister-list'})

for row in table.findAll('a'):
    print(row.text)