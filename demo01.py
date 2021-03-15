"""
import time
import json

def application(environ, start_response):
    headers = [('Content-type', 'application/json')]
    start_response('200 OK', headers)
    return bytes(json.dumps({'time': time.time()}), 'utf-8')
"""

"""
import time
import json
from twisted.web import server,resource
from twisted.internet import reactor, endpoints

class Simple(resource.Resource):
    isLeaf = True
    def reder_GET(self,request):
        request.responseHeaders.addRawHeader(b"content-type",b"application/json")
        return bytes(json.dump({'time':time.time()}),'utf8')

site = server.Site(Simple())
endpoints = endpoints.TCP4ServerEndpoint(reactor,8080)
endpoints.listen(site)
reactor.run()
"""

from aiohttp import web
import time

async def handle(request):
    return web.json_response({'time':time.time()})

if __name__ == '__main__':
    app = web.Application()
    app.router.add_get('/',handle)
    web.run_app(app)