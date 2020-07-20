
import requests
from bs4 import BeautifulSoup
import random

def get_movie():
    # #select a random genre 
    genre = random.choice(['action', 'action,comedy', 'adventure', 'animation', 'comedy', 'comedy,romance', 'crime', 'drama', 'fantasy', 'horror', 'mystery', 'romance', 'sci-fi', 'thriller'])

    URL = "https://www.imdb.com/search/title/?genres="+ genre +"&explore=title_type,genres&title_type=movie&ref_=adv_explore_rhs"
    r = requests.get(URL)

    soup = BeautifulSoup(r.content, 'html5lib')
    table = soup.find('div', attrs = {'class':'lister-list'})

    films = {}
    images = []

    #look for all the names of the movies that appear on that page
    for row in table.findAll('h3', attrs = {'class':'lister-item-header'}):
        films[(row.find('a').text)] = row.find('a')['href']

    for row in table.findAll('div', attrs = {'class':'lister-item-image float-left'}):
        images.append(row.find('img')['loadlate'])

    movie = random.choice(list(films.keys()))
    movie_image = images[list(films.keys()).index(movie)]

    URL = "https://www.imdb.com" + list(films.values())[list(films.keys()).index(movie)]
    r = requests.get(URL)

    soup = BeautifulSoup(r.content, 'html5lib')
    table = soup.find('div', attrs = {'class':'poster'})

    #select a random movie
    return  "Genre: " + genre + " | Movie: " + movie + "\n" + table.find('a')['href']

def get_info():
        #select a random genre 
    genre = random.choice(['action', 'action,comedy', 'adventure', 'animation', 'comedy', 'comedy,romance', 'crime', 'drama', 'fantasy', 'horror', 'mystery', 'romance', 'sci-fi', 'thriller'])

    URL = "https://www.imdb.com/search/title/?genres="+ genre +"&explore=title_type,genres&title_type=movie&ref_=adv_explore_rhs"
    r = requests.get(URL)

    soup = BeautifulSoup(r.content, 'html5lib')
    table = soup.find('div', attrs = {'class':'lister-list'})

    films = []

    #look for all the names of the movies that appear on that page
    for row in table.findAll('h3', attrs = {'class':'lister-item-header'}):
        films.append(row.find('a')['href'])

    return 'Genre: ' + genre + '\n' + 'https://www.imdb.com/' + random.choice(films)

if __name__ == '__main__': 
    print(get_info())