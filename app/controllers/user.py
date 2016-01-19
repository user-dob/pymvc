from aiohttp import web
from app.app import app

@app.get('/user')
async def index(request):
    body = "Hello user"
    return web.Response(body=body.encode('utf-8'))
