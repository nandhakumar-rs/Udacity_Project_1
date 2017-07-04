import webbrowser

'''This DocString explains that this is a class named movie_info'''


class movie_info():
    '''This DocString is the constructor which initialize the instance and
     here we are also initializing instance variables'''

    def __init__(self, title, story_line, poster, trailer):
        self.title = title
        self.story_line = story_line
        self.poster = poster
        self.trailer = trailer

    '''This DocString is the instance method,this method is called by the instace
       that has been created for this class'''

    def show_trailer(self):
        webbrowser.open(self.trailer)
