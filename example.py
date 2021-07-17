from starlette.applications import Starlette
from starlette.responses import HTMLResponse, PlainTextResponse, FileResponse
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
    username = request.query_params.get("username")
    password = request.query_params.get("password")

    if username == 'markus' and password == 'oleg':
        open("login.temp", "wt").write("logged in") # write file
        return HTMLResponse(success_html, media_type='text/html')
    
    else:
        return HTMLResponse(fail_html, media_type='text/html')

async def index(request):
    return HTMLResponse(index_html, media_type='text/html') 

routes = [
    Route('/', homepage),
    Route('/login', login),
    Route('/login.html', homepage),
    Route('/index.html', index),
    Mount('/', StaticFiles(directory="static/assets")),
]

app = Starlette(debug=True, routes=routes)

