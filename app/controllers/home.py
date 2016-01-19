from aiohttp import web
from app.app import app

@app.get('/')
@app.text
async def home(request):
    return "Hello world"


@app.get('/json')
@app.json
async def home(request):
    return {
        'name': 'Name'
    }



