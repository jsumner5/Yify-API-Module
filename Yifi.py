import requests;
class Yifi:

    #list the latest n(10 by default) movies released on the yifi website
    def fetchLatestMovies(self, limit=10):
        listLatestMovies = requests.get('https://yts.ag/api/v2/list_movies.json?limit=%d'%limit).json()
        listLatestMovies = listLatestMovies['data']['movies']
        for movie in listLatestMovies:
            print(movie['title'], ' Id:', movie['id'])

    # will search all the movies on the yifi website
    def searchMovies(self, searchTerm):
        listMovies = requests.get('https://yts.ag/api/v2/list_movies.json?quality=720p&query_term='+searchTerm).json()
        mCount = listMovies['data']['movie_count']
        if(mCount<1):
            print('no results found for: ',searchTerm)
            return
        listMovies = listMovies['data']['movies']
        print('Found ',mCount,' movies')
        for movie in listMovies:
            print(movie['title'],' Id:',movie['id'])

    #return the url of a movie, takes movie id as param
    def fetchMovieUrl(self,movieId):
        fetchMovie = requests.get('https://yts.ag/api/v2/movie_details.json?movie_id=%d'%movieId).json()
        fetchMovie = fetchMovie['data']['movie']
        print(fetchMovie['title'], ' Id:', fetchMovie['id'], ' url:', fetchMovie['url'])
        return fetchMovie['url']





