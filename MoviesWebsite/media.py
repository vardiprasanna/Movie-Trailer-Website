import webbrowser


class Movie():
    def __init__ (self, movie_name, movie_story, movie_wallpaper, movie_trailer):
        self.title= movie_name
        self.storyline= movie_story
        self.poster_image_url = movie_wallpaper
        self.trailer_youtube_url = movie_trailer


    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url )
    
