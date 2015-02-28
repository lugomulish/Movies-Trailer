import urllib
import json

import media
import moviesPage


def instanceMovie(movieName, movieTrailerUrl):
    """
    This function create a Movie class stance and return it.
    We use a :param moviename to find movie information by OMDB API and need
    proporcionate the  :param UrlTrailer YouTube API because OMDB not provided.
    :param movieName:
    :param movieTrailer:
    :return:
    """
    url = "http://www.omdbapi.com/?t=%s&y=&plot=short&r=json" % movieName
    #Get the data of Api url.
    response = urllib.urlopen(url)
    #Decoding the response data
    data = json.loads(response.read())
    #Stance the class with the data obtained from the OMDb API
    obj = media.Movie(data['Year'], data['Rated'], data['Released'], data['Runtime'], data['Genre'],
                            data['Writer'], data['Director'], data['Actors'], data['Language'], data['Country'],
                            data['Awards'], data['Metascore'], data['Poster'], data['Plot'], data['Title'],
                            movieTrailerUrl, data['imdbID'])
    #Return the Movie Object.
    return obj

#Make the stance of movies,
frozen = instanceMovie('frozen', 'https://www.youtube.com/embed/TbQm5doF_Uc')
aladin = instanceMovie('aladdin', 'https://www.youtube.com/embed/gWLa6y7Z2TE')
pussInBoots = instanceMovie('puss+in+boots','https://www.youtube.com/embed/55gmAtakjJ4')
ponyo = instanceMovie('ponyo', 'https://www.youtube.com/embed/bskgNOXbdiE')
theCatReturns = instanceMovie('The+Cat+Returns', 'https://www.youtube.com/embed/Gp-H_YOcYTM')
transformers = instanceMovie('Transformers', 'https://www.youtube.com/embed/gAjgXlvVexI')
transformers2 = instanceMovie('Transformers%3A+Revenge+of+the+Fallen', 'https://www.youtube.com/embed/zuz9PFtdgVw')
beautyAndTheBeast = instanceMovie('Beauty+And+The+Beast', 'https://www.youtube.com/embed/8xPkn3k5V00')
theLittleMermaid = instanceMovie('The+Little+Mermaid', 'https://www.youtube.com/embed/ZGZX5-PAwR8')
avergers = instanceMovie('The+avengers', 'https://www.youtube.com/embed/eOrNdBpGMv8')
theLordOfTheRings = instanceMovie('The+Lord+of+the+Rings%3A+The+Fellowship+of+the+Ring', 'https://www.youtube.com/embed'
                                                                                         '/V75dMMIW2B4')
thePunisher = instanceMovie('THE+PUNISHER', 'https://www.youtube.com/embed/bWpK0wsnitc')

#Creates a array with all stances of movies.
movies = [frozen, aladin, pussInBoots, ponyo, theCatReturns, transformers, transformers2, beautyAndTheBeast,
          theLittleMermaid, avergers, theLordOfTheRings, thePunisher]

#Create the Movies Trailers page with the array of the movies stances.
moviesPage.open_movies_page(movies)