#coding:utf8
import pymysql
import json
import logging
from BaseHandler import BaseHandler
from utils.response_code import RET


from tornado.web import RequestHandler

class HotelsHandler(BaseHandler):


    def get(self):
        cur = self.db.cursor(cursor=pymysql.cursors.DictCursor)
        logging.error("这个接口执行了")

        sql = "select hotel_id,hotel_name,detail_position_x,detail_position_y,district_code,hotel_type,hotel_introduce,hotel_address,reception_phone,service_fee from y_hotel_info_8"

        try:
            ret = cur.execute(sql)
        except Exception as e :
            logging.error(e)
            return self.write(dict(errno=RET.DBERR, errmsg="查询出错"))
        result = cur.fetchall()
        a = []
        if ret:
            for l  in result:
                # print(l)
                a.append(l)

        # logging.error(dict(data = a))
        self.db.close()
        self.write(dict(data = a))

# searchhotelrecord_31
class SearchHotelRecord(BaseHandler):
    def get(self):
        cur = self.db.cursor(cursor=pymysql.cursors.DictCursor)

        logging.error("这个接口执行了")

        sql = "select S.search_Id,S.price,S.search_Time,S.checkInDate,S.leaveDate,U.phone_number from searchhotelrecord_31 S left join y_user_info_1 U  on S.user_Id=U.user_id order by U.search_Id DESC limit 0,200"

        try:
            ret = cur.execute(sql)
        except Exception as e :
            logging.error(e)
            return self.write(dict(errno=RET.DBERR, errmsg="查询出错"))
        result = cur.fetchall()
        a = []
        if ret:
            for l  in result:
                print(l)

                if l["search_Time"]:


                   l["search_Time"] = l["search_Time"].strftime("%Y-%m-%d %H:%M:%S")

                if l["checkInDate"]:


                   l["checkInDate"] = l["checkInDate"].strftime("%Y-%m-%d")
                if l["leaveDate"]:


                   l["leaveDate"] = l["leaveDate"].strftime("%Y-%m-%d")

                a.append(l)

        # logging.error(dict(data = a))
        self.db.close()
        self.write(dict(data = a))
