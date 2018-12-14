# coding:utf-8
import os

from handlers import MyOrders
from tornado.web import StaticFileHandler
urls = [
    (r"/api/orders",MyOrders.OrdersHandlers),
    (r"/(.*)", StaticFileHandler,
        dict(path=os.path.join(os.path.dirname(__file__), "html"), default_filename="index.html"))












]
