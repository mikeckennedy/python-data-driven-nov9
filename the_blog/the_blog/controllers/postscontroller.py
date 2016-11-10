import pyramid_handlers
from the_blog.controllers.controller import BaseController
from the_blog.data.comments import Comment
from the_blog.data.posts import Post
import the_blog.data.db as db


class PostsController(BaseController):
    @pyramid_handlers.action(renderer='the_blog:templates/posts/details.pt')
    def details(self):
        # '/controller/{action=details}/{id}'
        url = self.data.get('id')
        if not url:
            self.redirect('/')

        session = db.session_factory()
        post = session.query(Post) \
            .filter(Post.url == url) \
            .first()

        if not post:
            self.redirect('/')

        post.comments.append(Comment(text="This is the first comment!"))
        session.commit()

        return {'post': post}
