import webbrowser


class Movie():
    """ This class provides a way to store movie related information
    Attributes:
        title: The movie title
        storyline: Storyline of the movie
        poster_image_url: Official poster image of the movie
        trailer_youtube_url: Youtube link of the movie trailer
    """
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Opens the movie trailer url
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
