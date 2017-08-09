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

jurassic_park = media.Movie(
    "Jurassic Park",
    "A science fiction adventure film about cloned dinosaurs.",
    "https://goo.gl/y26nSP",
    "https://www.youtube.com/watch?v=lc0UehYemQA")

lion_king = media.Movie(
    "Lion King",
    "Animated movie about Simba, a young lion.",
    "https://goo.gl/WphtiF",
    "https://www.youtube.com/watch?v=4sj1MT05lAA")

the_jungle_book = media.Movie(
    "The Jungle Book",
    "Animated movie about Mowgli, a feral child.",
    "https://goo.gl/TkGdnT",
    "https://www.youtube.com/watch?v=LNVTKXIK7q8")

movies = [spotlight, titanic, the_martian, jurassic_park,
          lion_king, the_jungle_book]

# Function to build the HTML file

fresh_tomatoes.open_movies_page(movies)
