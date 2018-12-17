#coding:utf8
import pymysql
import json
import logging
from BaseHandler import BaseHandler
from tornado.web import RequestHandler

class OrdersHandlers(BaseHandler):

    def get(self):

        # self.write('{"errno":1}')
        cur = self.db.cursor(cursor=pymysql.cursors.DictCursor)
        logging.error("这个接口执行了")
        sql = "select O.order_number ,O.order_date,O.price,O.booking_num,O.unit_price,O.pay_type,O.booking_checkin_date,O.booking_leave_date,O.order_type,O.order_state,H.hotel_name,H.hotel_address, U.nick_name,U.phone_number from y_order_record_3 O left join y_hotel_info_8 H on O.hotel_Id=H.hotel_Id left join y_user_info_1 U on H.user_id=U.user_id    order by O.order_id DESC limit 0,10"
        try:

            ret =cur.execute(sql)
        except Exception  as e:
            logging.error(e)
        result = cur.fetchall()
        a = []
        if ret:
            for l in result:
                print(l)
                logging.error(l)
                logging.error(l["order_date"])
                if l["order_date"]:


                   l["order_date"] = l["order_date"].strftime("%Y-%m-%d %H:%M:%S")
                if l["booking_checkin_date"]:


                   l["booking_checkin_date"] = l["booking_checkin_date"].strftime("%Y-%m-%d")
                if l["booking_leave_date"]:


                   l["booking_leave_date"] = l["booking_leave_date"].strftime("%Y-%m-%d")

                a.append(l)


        logging.error(dict(data = a))

        self.write(dict(data = a))
















