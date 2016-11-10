from the_blog.viewmodels.viewmodelbase import ViewModelBase


class CreatePostViewModel(ViewModelBase):
    def __init__(self):
        self.title = None
        self.url = None
        self.content = None
        self.error_msg = None

    def from_dict(self, data_dict):
        self.title = data_dict.get('title')
        self.url = data_dict.get('url')
        self.content = data_dict.get('content')

    def validate(self):
        if not self.title or not self.title.strip():
            self.error_msg = "You must specify a title"
            return False
        if not self.url or not self.url.strip():
            self.error_msg = "You must specify a url"
            return False
        if not self.content or not self.content.strip():
            self.error_msg = "You must specify some content"
            return False

        if self.url.find('/') >= 0 or self.url.find('\\') >= 0:
            self.error_msg = 'Url cannot contain slashes'
            return False

        return True
