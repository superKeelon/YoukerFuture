#coding:utf8

import pymysql
import json
import logging
from BaseHandler import BaseHandler
from utils.response_code import RET


from tornado.web import RequestHandler

class UserHandler(BaseHandler):
    def get(self):
        cur = self.db.cursor(cursor=pymysql.cursors.DictCursor)
        logging.error("这个接口执行了")
        sql = "select user_id, user_name,nick_name, phone_number, gender,reg_date  from y_user_info_1"
        try:
            ret = cur.execute(sql)
        except Exception as e:
            logging.error(e)
            return self.write(dict(errno=RET.DBERR, errmsg="查询出错"))
        result = cur.fetchall()

        a = []
        if ret:
            for l in result:
                print(l)
                logging.error(l)
                # logging.error(l["order_date"])
                if l["reg_date"]:


                   l["reg_date"] = l["reg_date"].strftime("%Y-%m-%d %H:%M:%S")

                a.append(l)



        logging.error(dict(data = a))
        self.db.close()

        self.write(dict(data = a))





