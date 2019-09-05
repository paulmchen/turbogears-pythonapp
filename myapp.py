from wsgiref.simple_server import make_server
from tg import expose, TGController, AppConfig


class MyController(TGController):

    @expose()
    def index(self):
        return 'Hello TurboGears!'


config = AppConfig(minimal=True, root_controller=MyController())
application = config.make_wsgi_app()

