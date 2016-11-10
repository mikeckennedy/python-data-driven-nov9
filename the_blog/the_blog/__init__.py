from pyramid.config import Configurator


def main(_, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=60*60)
    config.add_route('home', '/')
    config.scan()

    return config.make_wsgi_app()
