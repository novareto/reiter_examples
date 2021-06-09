from roughrider.routing.route import Routes
from horseman.response import reply
from fanstatic import Library, Resource


library = Library('reiter_middleware', 'static')
css = Resource(library, 'style.css')


routes = Routes()


@routes.register('/', methods=['GET'])
def index(request):
    css.need()
    return reply(
        200, "<html><head></head><body>Hello world</body></html>",
        {'Content-Type': 'text/html'}
    )
