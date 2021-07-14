from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles


async def homepage(request):
    return PlainTextResponse('This is the main page.')

routes = [
    Route('/', homepage),
    Mount('/static', StaticFiles(directory=".")),
]

app = Starlette(debug=True, routes=routes)
