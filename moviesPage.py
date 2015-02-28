import webbrowser
import os

# Scripts of the page.
main_page_head = '''
    <script type="text/javascript" charset="utf-8">
        $(document).ready(function(){
            //We create a modal for movies
            $('.modal-movie').leanModal();
        });

        //When the modal is closed, we stop all youtube Iframes
        $('.modal-movie').leanModal({
            complete: function() { $("iframe").each(function() {
                var src= $(this).attr('src');
                $(this).attr('src',src);
            }); } // Callback for Modal close
            }
        );

        //When the button is clicked, we hide the movie Information and show the Youtube Iframe.
        $(".play_trailer").click(function() {
            $(".modal_info").slideToggle("slow");
            $(".modal_trailer").slideToggle("slow");
        });

        //We show the YouTube Iframe and hide the movie Information.
        $(".play").click(function() {
            $(".modal_trailer").show();
            $(".modal_info").hide();
        })

        //We hide the YouTube Iframe and show the movie Information.
        $(".info").click(function() {
            $(".modal_trailer").hide();
            $(".modal_info").show();
        })
    </script>
'''

# The main page layout, title bar and styles.
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no"/>
    <title>Movie Trailers</title>

    <!-- CSS  -->
    <!--Import materialize.css-->
    <link type="text/css" rel="stylesheet" href="css/materialize.min.css"
          media="screen,projection"/>
    <link type="text/css" rel="stylesheet" href="css/style.css"
          media="screen,projection"/>
    <script type="text/javascript" src="https://code.jquery.com/jquery-2.1.1.min.js"></script>
    <script type="text/javascript" src="js/materialize.min.js"></script>

</head>
<body>
<div class="navbar-fixed">
    <nav class="light-blue lighten-1 navbar-fixed" role="navigation">
        <div class="container">
            <div class="nav-wrapper"><a id="logo-container" href="#" class="brand-logo">Lugo-Movies</a>
                <div class="col s12">
                    <a href="#!" class="brand-logo">Logo</a>
                    <ul class="right hide-on-med-and-down">
                    </ul>
                </div>
            </div>
        </div>
    </nav>
</div>
<div class="container">
    <div class="section">

        <h1 class="center-align">Mensaje Principal</h1>
        <!--Movies Seccion-->
        <div class="row">
            {movie_tiles}
        </div>

    </div>

    <br><br>

    <div class="section">

    </div>
</div>

<footer class="page-footer orange">
    <div class="container">
        <div class="row">
            <div class="col l6 s12">
                <h5 class="white-text">Company Bio</h5>

                <p class="grey-text text-lighten-4">We are a team of college students working on this project like it's
                    our full time job. Any amount would help support and continue development on this project and is
                    greatly appreciated.</p>


            </div>
            <div class="col l3 s12">
                <h5 class="white-text">Settings</h5>
                <ul>
                    <li><a class="white-text" href="#!">Link 1</a></li>
                    <li><a class="white-text" href="#!">Link 2</a></li>
                    <li><a class="white-text" href="#!">Link 3</a></li>
                    <li><a class="white-text" href="#!">Link 4</a></li>
                </ul>
            </div>
            <div class="col l3 s12">
                <h5 class="white-text">Connect</h5>
                <ul>
                    <li><a class="white-text" href="#!">Link 1</a></li>
                    <li><a class="white-text" href="#!">Link 2</a></li>
                    <li><a class="white-text" href="#!">Link 3</a></li>
                    <li><a class="white-text" href="#!">Link 4</a></li>
                </ul>
            </div>
        </div>
    </div>
    <div class="footer-copyright">
        <div class="container">
            Made by <a class="orange-text text-lighten-3" href="http://materializecss.com">Materialize</a>
        </div>
    </div>
</footer>


<!--Import jQuery before materialize.js-->


</body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col s3">
    <div class="card center-align">
        <div class="card-image waves-effect waves-block waves-light">
            <img class="activator" src="{movie_poster}" height='300px'>
        </div>
        <div class="valign-wrapper" style="height:90px;">
            <h5 class="valign">{movie_title}</h5>
        </div>
        <a class="btn-floating btn-large waves-effect waves-light green modal-movie play" href="#{movie_id}">
            <i class="mdi-av-play-arrow"></i>
        </a>
        <a class="btn-floating btn-large waves-effect waves-light red modal-movie info" href="#{movie_id}">
            <i class="mdi-navigation-more-horiz"></i>
        </a>


    </div>
</div>

<!-- Modal Structure -->
<div id="{movie_id}" class="modal modal-fixed-footer">
    <div class="modal-content">
        <div class="modal_info">
            <div class="row">
                <h4 class="center-align">{movie_title}</h4>
                <div class="col s3">
                    <div class="card-image waves-effect waves-block waves-light center-align">
                        <img class="responsive-img"
                        src="{movie_poster}">
                        <a class="btn-floating btn-large waves-effect waves-light green modal-play play_trailer" href="#">
                            <i class="mdi-av-play-arrow" ></i>
                        </a>
                    </div>
                </div>
                <div class="col s4 left-align">
                    <b>YEAR:</b> {movie_year}
                    <br/>
                    <b>RATED:</b> {movie_rated}
                    <br/>
                    <b>RELEASED:</b> {movie_released}
                    <br/>
                    <b>RUNTIME:</b> {movie_runtime}
                    <br/>
                    <b>GENRE:</b> {movie_genre}
                    <br/>
                    <b>WRITER:</b> {movie_writer}
                    <br/>
                    <b>DIRECTOR:</b> {movie_director}
                </div>
                <b class="center-align">Plot</b></br>
                <div class="col s4 left-align">
                    {movie_plot}
                </div>
            </div>
        </div>
        <div class="modal_trailer" style="display:none;">
            <iframe id = "trailer{movie_id}" class="trailer" width="640" height="390" src="{movie_trailer}" frameborder="0" allowfullscreen></iframe>
            <div class = "cerrarVideo">CERRAR</div>
        </div>
    </div>
</div>
'''


def create_movie_titles_content(movies):
    """
    We create a html content for every movie in the movies array.
    :param movies:
    :return:
    """
    content = ''
    for movie in movies:

        # Append the info for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            movie_year=movie.year,
            movie_rated=movie.rated,
            movie_released=movie.released,
            movie_runtime=movie.runtime,
            movie_genre=movie.genre,
            movie_writer=movie.writer,
            movie_director=movie.director,
            movie_actor=movie.actor,
            movie_language=movie.language,
            movie_country=movie.country,
            movie_awards=movie.awards,
            movie_metascore=movie.metascore,
            movie_poster=movie.poster,
            movie_plot=movie.plot,
            movie_trailer=movie.trailer,
            movie_id=movie.id
        )

    return content

def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('movies-trailer.html', 'w')

  # Replace the placeholder for the movie information with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_titles_content(movies))

  # Output the file
  output_file.write(rendered_content+main_page_head)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible