import pyramid_handlers
from sqlalchemy.orm import joinedload
from the_blog.controllers.controller import BaseController
from the_blog.data.posts import Post
from the_blog.infrastructure.suppressor import suppress
import the_blog.data.db as db


class HomeController(BaseController):
    @pyramid_handlers.action(renderer='the_blog:templates/home/index.pt')
    def index(self):
        session = db.session_factory()
        all_posts = session.query(Post).\
            options(joinedload('comments')).\
            all()

        return {'posts': all_posts}

    @pyramid_handlers.action(renderer='the_blog:templates/home/about.pt')
    def about(self):
        return {}

    @suppress()
    def not_to_show(self):
        print("don't execute this!")

    @pyramid_handlers.action()
    def setup_db(self):
        session = db.session_factory()

        posts = [
            Post(title='The first post', content='Contents of the first post...', url='first'),
            Post(title='The second post', content='Contents of the 2nd post...', url='second-post'),
            Post(title='The last post', content='Contents of the last post...', url='last'),
        ]
        for p in posts:
            session.add(p)

        session.commit()
        self.redirect('/')
