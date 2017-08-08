import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life","https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)

titanic = media.Movie("Titanic", "Fictionalized account of the sinking of the RMS Titanic.", "https://en.wikipedia.org/wiki/Titanic_(1997_film)#/media/File:Titanic_poster.jpg", "https://www.youtube.com/watch?v=zCy5WQ9S4c0")

#print (titanic.storyline)
#titanic.show_trailer()

movies = [toy_story, titanic]
#fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
