import webbrowser


class movie_info():
    def __init__(self, title, story_line, poster, trailer):
        self.title = title
        self.story_line = story_line
        self.poster = poster
        self.trailer = trailer

    def show_trailer(self):
        webbrowser.open(self.trailer)
