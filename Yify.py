# Python class that can be used to search the yifi db
# All results are returned as arrays of dicts
# Example output:
# {'id': 5548, 'url': 'https://yts.ag/movie/the-abyss-1989', 'title': 'The Abyss'}
import requests


class Yify:

    def __init__(self):
        # set default options
        self.quality = '720'
        self.limit = '20'

    # methods to set options
    def set_limit(self, limit):
        self.limit = str(limit)

    def set_quality(self, quality):
        self.quality = quality

    # Returns an array of the most recently added movies
    def get_latest_movies(self):
        uri = 'https://yts.ag/api/v2/list_movies.json?limit='+self.limit
        latest_movies = requests.get(uri).json()
        results = []
        latest_movies = latest_movies['data']['movies']
        for movie in latest_movies:
            movie_dict = {}
            movie_dict.update({'title': movie['title'], 'id': movie['id'], 'url': movie['url']})
            results.append(movie_dict)
        return results

    # Search movies using term and returns an array of movies, each movie as a dict
    def get_movies_by_term(self, search_term):
        uri = 'https://yts.ag/api/v2/list_movies.json?quality=' + self.quality + '&query_term=' + search_term
        list_movies = requests.get(uri).json()
        results = []
        movie_count = list_movies['data']['movie_count']
        if movie_count < 1:
            print('no results found for: ', search_term)
            return
        list_movies = list_movies['data']['movies']
        for movie in list_movies:
            movie_dict = {}
            movie_dict.update({'title': movie['title'], 'id': movie['id'], 'url': movie['url']})
            results.append(movie_dict)
        return results





