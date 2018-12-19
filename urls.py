# coding:utf-8
import os

from handlers import MyOrders,UserHandler,HotelHandler

from tornado.web import StaticFileHandler
urls = [
    (r"/api/orders",MyOrders.OrdersHandlers),
    (r"/api/hotels",HotelHandler.HotelsHandler),
    (r"/api/searchRecord",HotelHandler.SearchHotelRecord),

    (r"/api/users",UserHandler.UserHandler),
    (r"/(.*)", StaticFileHandler,
        dict(path=os.path.join(os.path.dirname(__file__), "html"), default_filename="index.html"))












]
