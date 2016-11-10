import datetime


class Post:
    title = None
    pub_date = datetime.datetime.now()
    content = None
    url = None

    def __init__(self, title, content, url):
        self.url = url
        self.content = content
        self.title = title
