from pyramid.config import Configurator
import the_blog.controllers.homecontroller as home
import the_blog.controllers.postscontroller as posts
import the_blog.controllers.apicontroller as api


def main(_, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.include('pyramid_handlers')
    config.add_static_view('static', 'static', cache_max_age=60 * 60)
    # config.add_route('home', '/')
    config.add_handler('home_ctrl', '/', handler=home.HomeController, action='index')
    config.add_handler('posts_single_api', '/api/posts/{id}', handler=api.ApiController, action='posts_singular')
    init_routes(config, home.HomeController, 'home')
    init_routes(config, posts.PostsController, 'posts')
    init_routes(config, api.ApiController, 'api')
    config.scan()

    return config.make_wsgi_app()


def init_routes(config, handler, prefix):
    config.add_handler(prefix + '_ctrl_action', '/' + prefix + '/{action}', handler=handler)
    config.add_handler(prefix + '_ctrl_action/', '/' + prefix + '/{action}/', handler=handler)
    config.add_handler(prefix + '_ctrl_action/id', '/' + prefix + '/{action}/{id}', handler=handler)
