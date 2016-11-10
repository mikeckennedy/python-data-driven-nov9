import json

import pyramid_handlers
import the_blog.data.db as db
from sqlalchemy.orm import joinedload
from the_blog.controllers.controller import BaseController
from the_blog.data.posts import Post
from the_blog.viewmodels.create_post_viewmodel import CreatePostViewModel


class ApiController(BaseController):
    # /api/posts
    @pyramid_handlers.action(renderer='json', request_method='GET')
    def posts(self):
        session = db.session_factory()
        all_posts = session.query(Post).\
            options(joinedload('comments')).\
            order_by(Post.pub_date.desc())

        all_posts_data = [
            {'title': p.title, 'url': p.url, 'id': p.id, 'data': str(p.pub_date)}
            for p in all_posts
            # if p.is_published
        ]

        return {'posts': all_posts_data}

    @pyramid_handlers.action(renderer='json')
    def posts_singular(self):
        post_id = self.data.get('id')
        if not post_id:
            return {'error': 'not found'}

        session = db.session_factory()
        post = session.query(Post).\
            filter(Post.id == post_id).\
            options(joinedload('comments')).one()

        return {
            'title': post.title,
            'url': post.url,
            'id': post.id,
            'data': str(post.pub_date),
            'content': post.content
        }

    @pyramid_handlers.action(renderer='json', request_method='POST', name='posts')
    def posts_post(self):
        data = self.request.json_body
        vm = CreatePostViewModel()
        vm.from_dict(data)

        if not vm.validate():
            return {'error': vm.error_msg}

        session = db.session_factory()
        p = Post(title=vm.title, url=vm.url, content=vm.content)
        session.add(p)
        session.commit()

        return {
            'status': 'created',
            'title': p.title,
            'url': p.url,
            'id': p.id,
            'data': str(p.pub_date),
            'content': p.content
        }
