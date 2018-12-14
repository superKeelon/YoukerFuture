import pymysql
import json
from BaseHandler import BaseHandler
from tornado.web import RequestHandler

class OrdersHandlers(RequestHandler):

    def get(self):

        self.write('{"errno":1}')







