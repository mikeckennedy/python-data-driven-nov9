from pyramid.config import Configurator
import the_blog.controllers.homecontroller as home


def main(_, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.include('pyramid_handlers')
    config.add_static_view('static', 'static', cache_max_age=60 * 60)
    # config.add_route('home', '/')
    config.add_handler('home_ctrl', '/', handler=home.HomeController, action='index')
    init_routes(config, home.HomeController, 'home')
    config.scan()

    return config.make_wsgi_app()


def init_routes(config, handler, prefix):
    config.add_handler(prefix + '_ctrl_action', '/' + prefix + '/{action}', handler=handler)
    config.add_handler(prefix + '_ctrl_action/', '/' + prefix + '/{action}/', handler=handler)
    config.add_handler(prefix + '_ctrl_action/id', '/' + prefix + '/{action}/{id}', handler=handler)
