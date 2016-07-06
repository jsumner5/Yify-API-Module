from Yifi import Yifi;
#create a instance of YifiApi
YA = Yifi()
#search yifi with the term "titanic"
YA.searchMovies("titanic")
#pass the movie id of titanic to print the url of it
YA.fetchMovieUrl(3897)
