# Import fresh_tomatoes which will take movies list gives a visual output and generates the web page
import fresh_tomatoes

#media file contains the Class Movie which will used to generate instances of the movies
import media


#Generating the instances of the movies
ice_age = media.Movie("Ice Age", " Story of animals which lived in Ice age",
                      "http://hdqwalls.com/download/ice-age-5-collision-course-2048x1152.jpg",
                      "https://www.youtube.com/watch?v=Ohq6NmKMja8")

Kabali = media.Movie("Kabali","Hopeless Story. Don't waste your time by asking it",
                     "http://www.stage3.in/wp-content/uploads/2016/06/Kabali-poster.jpg",
                     "https://www.youtube.com/watch?v=9mdJV5-eias") 

Shivaji = media.Movie("Shivaji","super entertaining film of a NRI who plans to serve india",
                      "https://upload.wikimedia.org/wikipedia/en/c/ce/Sivaji_The_Boss.jpg",
                      "https://www.youtube.com/watch?v=Y7znvurIqRA")


kannathil_muthamittal = media.Movie("kannathil muthamittal",
                                    " Story of Child and parent directed by maniratnam",
                                    "https://aparnasblog.files.wordpress.com/2007/04/wall3.jpg",
                                    "https://www.youtube.com/watch?v=ez1Ea0T98c8")


Enthiran = media.Movie("Enthiran", "Story of Robot which truns into an evil",
                       "http://wfiles.brothersoft.com/e/endhiran-poster_80485-1600x1200.jpg",
                       "https://www.youtube.com/watch?v=CSc6BtyCP5k")



# Make a list of generated instances to pass as an argument to the next method
movies = [ice_age, Kabali, Shivaji, kannathil_muthamittal , Enthiran]


#call open_movies_page method to generate the web page
fresh_tomatoes.open_movies_page(movies)
