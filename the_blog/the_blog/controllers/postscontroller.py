import pyramid_handlers
from the_blog.controllers.controller import BaseController
from the_blog.data.comments import Comment
from the_blog.data.posts import Post
import the_blog.data.db as db
from the_blog.viewmodels.create_post_viewmodel import CreatePostViewModel


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

        # post.comments.append(Comment(text="This is the first comment!"))
        # session.commit()

        return {'post': post}

    @pyramid_handlers.action(renderer='the_blog:templates/posts/create_post.pt',
                             request_method='GET',
                             name='create_post')
    def create_post_get(self):
        vm = CreatePostViewModel()
        return vm.to_dict()

    @pyramid_handlers.action(renderer='the_blog:templates/posts/create_post.pt',
                             request_method='POST',
                             name='create_post')
    def create_post_post(self):
        vm = CreatePostViewModel()
        vm.from_dict(self.data)

        if not vm.validate():
            return vm.to_dict()

        session = db.session_factory()
        session.add(Post(title=vm.title, url=vm.url, content=vm.content))
        session.commit()

        self.redirect('/posts/details/' + vm.url)
