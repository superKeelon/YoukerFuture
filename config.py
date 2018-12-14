# coding:utf-8
# setting有一个静态文件目录。
import os
#Application配置。
#
settings = {

    "static_path":os.path.join(os.path.dirname(__file__),"static"),
    "template_path":os.path.join(os.path.dirname(__file__),"template"),
    "debug":True,
    "cookie_secret":"FhLXI+BRRomtuaG47hoXEg3JCdi0BUi8vrpWmoxaoyI=",
    "xsrf_cookies":True,
}
# settings = dict(
#         static_path=os.path.join(os.path.dirname(__file__), "static"),
#
#         cookie_secret="FhLXI+BRRomtuaG47hoXEg3JCdi0BUi8vrpWmoxaoyI=",
#         xsrf_cookies=True,
#         debug=True
#     )
#mysql
mysql_options = dict(
    host='127.0.0.1',
    database='ihome',
    user='root',
    password='dcdell88',
    charset='utf8',


)
#redis
redis_options = dict(

    host="127.0.0.1",
    port=6379
)
# 当前文件的log里面。
log_file = os.path.join(os.path.dirname(__file__),"logs/log")

#设置日志等级。
log_level = "debug"
session_expires_seconds = 86400

#配置一个密码混淆的值
passwd_hash_key = "ihome@^*"