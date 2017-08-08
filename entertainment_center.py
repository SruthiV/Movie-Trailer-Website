import fresh_tomatoes
import media

# Contains movie data and executes the function to build the HTML file.

spotlight = media.Movie(
    "Spotlight",
    "A true crime drama about an investigation into a church scandal.",
    "https://goo.gl/3K2K4W",
    "https://www.youtube.com/watch?v=EwdCIpbTN5g")

titanic = media.Movie(
    "Titanic",
    "Fictionalized account of the sinking of the RMS Titanic.",
    "https://goo.gl/laexwR",
    "https://www.youtube.com/watch?v=zCy5WQ9S4c0")

the_martian = media.Movie(
    "The Martian",
    "A science fiction film about an astronaut stranded on Mars.",
    "https://goo.gl/TQsKNK",
    "https://www.youtube.com/watch?v=ej3ioOneTy8")

movies = [spotlight, titanic, the_martian]

# Function to build the HTML file

fresh_tomatoes.open_movies_page(movies)
