from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('.models')
    config.include('.views')
    config.include('.routes')
    config.scan()
    return config.make_wsgi_app()
