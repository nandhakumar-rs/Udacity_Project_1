import movie
import fresh_tomatoes

batman = movie.movie_info("Dark Knight",
                          " Batman has been able to keep a tight lid on crime in Gotham City.",
                          "http://host.trivialbeing.org/up/tdk-jul1-dark-knight-poster-stupidbats.jpg",
                          "https://www.youtube.com/watch?v=_PZpmTj1Q8Q")
inception = movie.movie_info("Inception",
                             "Inception is a 2010 science fiction film",
                             "http://cdn.collider.com/wp-content/uploads/Inception-movie-poster-4.jpg",
                             "https://www.youtube.com/watch?v=YoHD9XEInc0")
facebook = movie.movie_info("Social Network",
                            "In 2003, Harvard undergrad and computer genius Mark Zuckerberg (Jesse Eisenberg) begins work on a new concept that eventually turns into the global social network known as Facebook.",
                            "http://2.bp.blogspot.com/_jJHM9-HXtXI/TRzw26ISM7I/AAAAAAAAAPo/Db9lm69eZw8/s1600/the-social-network-movie-poste.jpg",
                            "https://www.youtube.com/watch?v=2RB3edZyeYw")
steve_jobs = movie.movie_info("Jobs",
                              "College dropout Steve Jobs (Ashton Kutcher), together with his friend, technical whiz-kid Steve Wozniak (Josh Gad), sparks a revolution in home computers with the invention of the Apple 1 in 1976.",
                              "http://www.cinemum.net/media/k2/items/cache/dd45d054dfce696b68bc0b43a11d1bfe_XL.jpg",
                              "https://www.youtube.com/watch?v=FrvkCS0ZGPU")
x_men = movie.movie_info("Logan",
                         "In the near future, a weary Logan (Hugh Jackman) cares for an ailing Professor X (Patrick Stewart) at a remote outpost on the Mexican border",
                         "http://www.joblo.com/posters/images/full/logan-poster-3.jpg",
                         "https://www.youtube.com/watch?v=Div0iP65aZo")
art = movie.movie_info("Diagonal Art",
                       "Diagonal art program using python turtle",
                       "art.PNG",
                       "https://www.youtube.com/watch?v=p_219d8HVHQ&feature=youtu.be")
favorite = [batman, inception, facebook, steve_jobs, x_men, art]
fresh_tomatoes.open_movies_page(favorite)
