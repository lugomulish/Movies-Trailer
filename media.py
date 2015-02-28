import webbrowser


class Movie():

    def __init__(self, movie_year, movie_rated, movie_released, movie_runtime, movie_genre, movie_writer,
                 movie_director, movie_actors, movie_languaje, movie_country, movie_awards, movie_metascore,
                 movie_poster, movie_plot, movie_title, movie_trailer, movie_id):
        """
        We define the constructor method for Movies.
        :param movie_year:
        :param movie_rated:
        :param movie_released:
        :param movie_runtime:
        :param movie_genre:
        :param movie_writer:
        :param movie_director:
        :param movie_actors:
        :param movie_languaje:
        :param movie_country:
        :param movie_awards:
        :param movie_metascore:
        :param movie_poster:
        :param movie_plot:
        :param movie_title:
        :param movie_trailer:
        :param movie_id:
        :return:
        """
        self.title = movie_title
        self.year = movie_year
        self.rated = movie_rated
        self.released = movie_released
        self.runtime = movie_runtime
        self.genre = movie_genre
        self.writer = movie_writer
        self.director = movie_director
        self.actor = movie_actors
        self.language = movie_languaje
        self.country = movie_country
        self.awards = movie_awards
        self.metascore = movie_metascore
        self.poster = movie_poster
        self.plot = movie_plot
        self.trailer = movie_trailer
        self.id = movie_id