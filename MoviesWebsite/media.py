#import webbrowser to open url link and display the trailer of the movie
import webbrowser



#create a class of movie
class Movie():

    #constructor to assign the content of the movie
    def __init__ (self, movie_name, movie_story, movie_wallpaper, movie_trailer):
        self.title= movie_name
        self.storyline= movie_story
        self.poster_image_url = movie_wallpaper
        self.trailer_youtube_url = movie_trailer


    #method to open the trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url )
    
