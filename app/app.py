import asyncio
from aiohttp import web
import json

class App:

    def __init__(self):
        self.routes = []

    def get(self, path):
        def decorator(handle):
            self.routes.append(('GET', path, handle))
            return handle
        return decorator

    def post(self, path):
        def decorator(handle):
            self.routes.append(('POST', path, handle))
            return handle
        return decorator

    def put(self, path):
        def decorator(handle):
            self.routes.append(('PUT', path, handle))
            return handle
        return decorator

    def text(self, handle):
        async def decorator(request):
            body = await handle(request)
            return web.Response(body=body.encode('utf-8'))
        return decorator

    def json(self, handle):
        async def decorator(request):
            body = await handle(request)
            body = json.dumps(body)
            return web.Response(body=body.encode('utf-8'), headers={'Content-Type': 'application/json'})
        return decorator

    async def init(self, loop):
        app = web.Application(loop=loop)

        for (method, path, handler) in self.routes:
            app.router.add_route(method, path, handler)

        srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8080)

        print("Server started at http://127.0.0.1:8080")
        return srv

        pass

    def run(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.init(loop))
        loop.run_forever()


app = App()