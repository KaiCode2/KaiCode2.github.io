
class Post(object):
    """Class for blog posts."""
    def __init__(self, header, brief, link):
        super(Post, self).__init__()
        self.header = header
        self.brief = brief
        self.link = link
