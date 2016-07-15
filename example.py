from Yifi import Yifi
# Create a instance of YifiApi
YA = Yifi()
# Assigne searchTerm to "The Abyss"
searchTerm="The Abyss"

# assign movies to the returned array
movies = YA.getSearchMovies(searchTerm)
# Iterate through movies and print the results
for movie in movies:
    print(movie)

