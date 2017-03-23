# Yify Module/Library (Yify Movie API Wrapper)
## Dependencies:
*requests
## Easy install:
coming soon :)
For now download the zip

## Example:
```
# Import lib
from Yify import *

# Create a instance of Yify
yify = Yify()

# make call to yify and get movies
movies = yify.get_movies_by_term('Star Wars')

# Iterate through movies and print the results
for movie in movies:
    print(movie)
```
results:
```
{'title': 'Star Wars: Episode VII - The Force Awakens', 'id': 5315, 'url': 'https://yts.ag/movie/star-wars-episode-vii-the-force-awakens-2015'}
{'title': 'Star Wars: Episode VI - Return of the Jedi', 'id': 2863, 'url': 'https://yts.ag/movie/star-wars-episode-vi-return-of-the-jedi-1983'}
{'title': 'Star Wars: Episode V - The Empire Strikes Back', 'id': 2862, 'url': 'https://yts.ag/movie/star-wars-episode-v-the-empire-strikes-back-1980'}
{'title': 'Star Wars: Episode III - Revenge of the Sith', 'id': 2861, 'url': 'https://yts.ag/movie/star-wars-episode-iii-revenge-of-the-sith-2005'}
{'title': 'Star Wars: Episode II - Attack of the Clones', 'id': 2860, 'url': 'https://yts.ag/movie/star-wars-episode-ii-attack-of-the-clones-2002'}
{'title': 'Star Wars: Episode I - The Phantom Menace', 'id': 2859, 'url': 'https://yts.ag/movie/star-wars-episode-i-the-phantom-menace-1999'}
{'title': 'Star Wars: Episode IV - A New Hope', 'id': 2858, 'url': 'https://yts.ag/movie/star-wars-episode-iv-a-new-hope-1977'}
```
Thats It !
