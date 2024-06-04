import tornado.web

import json
from models import mongo_db

class MongoHandler(tornado.web.RequestHandler):