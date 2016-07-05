from Yifi import Yifi;
#create a instance of YifiApi
YTS = Yifi()
#search all movies for the keywords I am
YTS.searchMovies("I am ")
#get the url for the movie I am Legend
YTS.fetchMovieUrl(1551)
