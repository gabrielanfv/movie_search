import requests
from bs4 import BeautifulSoup
import random

#select a random genre 
genre = random.choice(['action', 'action,comedy', 'adventure', 'animation', 'comedy', 'comedy,romance', 'crime', 'drama', 'fantasy', 'horror', 'mystery', 'romance', 'sci-fi', 'thriller'])
print(genre)

URL = "https://www.imdb.com/search/title/?genres="+ genre +"&explore=title_type,genres&title_type=movie&ref_=adv_explore_rhs"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')
table = soup.find('div', attrs = {'class':'lister-list'})

films = []

#look for all the names of the movies that appear on that page
for row in table.findAll('h3', attrs = {'class':'lister-item-header'}):
    films.append(row.find('a').text)


#select a random movie
print(random.choice(films))