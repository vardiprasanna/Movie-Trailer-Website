import fresh_tomatoes
import media

ice_age = media.Movie("Ice Age", " Story of animals which lived in Ice age", "http://hdqwalls.com/download/ice-age-5-collision-course-2048x1152.jpg","https://www.youtube.com/watch?v=Ohq6NmKMja8")

Kabali = media.Movie("Kabali","Hopeless Story. Don't waste your time by asking it","http://www.stage3.in/wp-content/uploads/2016/06/Kabali-poster.jpg","https://www.youtube.com/watch?v=9mdJV5-eias") 

Shivaji = media.Movie("Shivaji","super entertaining film of a NRL who plans to serve india through his good deeds","https://upload.wikimedia.org/wikipedia/en/c/ce/Sivaji_The_Boss.jpg","https://www.youtube.com/watch?v=Y7znvurIqRA")


kannathil_muthamittal = media.Movie("kannathil muthamittal"," Story of Child and parent directed by maniratnam","https://aparnasblog.files.wordpress.com/2007/04/wall3.jpg","https://www.youtube.com/watch?v=ez1Ea0T98c8")


Enthiran = media.Movie("Enthiran", "Story of Robot which truns into an evil", "http://wfiles.brothersoft.com/e/endhiran-poster_80485-1600x1200.jpg","https://www.youtube.com/watch?v=CSc6BtyCP5k")


movies = [ice_age, Kabali, Shivaji, kannathil_muthamittal , Enthiran]

fresh_tomatoes.open_movies_page(movies)
