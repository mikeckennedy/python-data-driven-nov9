import pyramid_handlers
from the_blog.controllers.controller import BaseController
from the_blog.data.posts import Post
from the_blog.infrastructure.suppressor import suppress


class HomeController(BaseController):

    @pyramid_handlers.action(renderer='the_blog:templates/home/index.pt')
    def index(self):
        all_posts = [
            Post('The first post', 'Contents of the first post...', 'first'),
            Post('The second post', 'Contents of the 2nd post...', 'second-post'),
            Post('The last post', 'Contents of the last post...', 'last'),
        ]

        return {'posts': all_posts}

    @pyramid_handlers.action(renderer='the_blog:templates/home/about.pt')
    def about(self):
        return {}

    @suppress()
    def not_to_show(self):
        print("don't execute this!")