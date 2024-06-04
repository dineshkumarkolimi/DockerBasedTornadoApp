import tornado.ioloop
import tornado.web

from handlers import MainHandler
from handlers import MainHandler
from handlers import MainHandler

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/users", MainHandler),
        (r"/mongo", MainHandler)],
        template_path='../Nginx/templates',
        static_path='../Nginx/static')

if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
    