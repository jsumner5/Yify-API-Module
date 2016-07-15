# Python class that can be used to search the yifi db
# All results are returned as arrays of dicts
# Example: {'id': 5548, 'url': 'https://yts.ag/movie/the-abyss-1989', 'title': 'The Abyss'}
import requests;
class Yifi:

    # Returns an array of the latest n(10 by default) movies released on the yifi website, each movie as a dict
    def getLatestMovies(self, limit=10):
        listLatestMovies = requests.get('https://yts.ag/api/v2/list_movies.json?limit=%d'%limit).json()
        results = []
        listLatestMovies = listLatestMovies['data']['movies']
        for movie in listLatestMovies:
            dictmovie = {}
            dictmovie.update({'title': movie['title'], 'id': movie['id'], 'url': movie['url']})
            results.append(dictmovie)
        return results



    # Search movies using term and returns an array of movies, each movie as a dict
    def getSearchMovies(self, searchTerm):
        listMovies = requests.get('https://yts.ag/api/v2/list_movies.json?quality=720p&query_term=' + searchTerm).json()
        results =[]
        mCount = listMovies['data']['movie_count']
        if (mCount < 1):
            print('no results found for: ', searchTerm)
            return
        listMovies = listMovies['data']['movies']
        print('Found ', mCount, ' movies')
        for movie in listMovies:
            dictmovie={}
            dictmovie.update({'title':movie['title'],'id':movie['id'],'url':movie['url']})
            results.append(dictmovie)
        return results





