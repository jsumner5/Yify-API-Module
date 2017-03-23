from Yify import *
# Create a instance of Yify
yify = Yify()


# Assign movies to the returned array
movies = yify.get_movies_by_term('Star Wars')

# Iterate through movies and print the results
for movie in movies:
    print(movie)

