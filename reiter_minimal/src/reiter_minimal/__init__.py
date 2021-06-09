from roughrider.routing.route import Routes
from horseman.response import reply


routes = Routes()


@routes.register('/', methods=['GET'])
def index(request):
    return reply(200, "Hello world")
