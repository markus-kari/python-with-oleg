from starlette.applications import Starlette
from starlette.responses import HTMLResponse, PlainTextResponse
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles

# Bad practice to preload all HTML -> better to do this in method where it needs it
fail_html = open("static/fail.html", "rt").read()
index_html = open("static/index.html", "rt").read()
login_html = open("static/login.html", "rt").read()
success_html = open("static/success.html", "rt").read()


async def homepage(request):
    try:
        state = open("login.temp", "rt").read() # read file
    except FileNotFoundError:
        state = ""
        open("login.temp", "xt") # create file

    if state == "logged in":
        return HTMLResponse(index_html, media_type='text/html')

    return HTMLResponse(login_html, media_type='text/html')

async def login(request):
    print(request.query_params.get("username"))
    print(request.query_params.get("password"))

    open("login.temp", "wt").write("hallo") # write file

    return PlainTextResponse("nothing is happening yet")

routes = [
    Route('/', homepage),
    Route('/login', login),
    Mount('/', StaticFiles(directory="static"), name="static"),
]

app = Starlette(debug=True, routes=routes)

