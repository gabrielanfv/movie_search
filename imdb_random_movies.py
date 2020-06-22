import requests
from bs4 import BeautifulSoup
import random

genre = random.choice(['action', 'action,comedy', 'adventure', 'animation', 'comedy', 'comedy,romance', 'crime', 'drama', 'fantasy', 'horror', 'mystery', 'romance', 'sci-fi', 'thriller'])
print(genre)

# URL_genre = 'https://www.imdb.com/search/title/?genres='+ genre +'&explore=title_type,genres&title_type=movie&ref_=adv_explore_rhs'
# r = requests.get(URL_genre)

URL = "https://www.imdb.com/search/title/?genres="+ genre +"&explore=title_type,genres&title_type=movie&ref_=adv_explore_rhs"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

film = random.randrange(1,51)

table = soup.find('div', attrs = {'class':'lister-list'})

films = table.find('div', attrs = {'class':'lister-item mode-advanced'})

for row in films.findAll('a'):
    print(row.text)