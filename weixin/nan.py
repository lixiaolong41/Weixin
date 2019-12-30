from weixin.config import *
import pymysql
db = pymysql.connect(host=MYSQL_HOST, username=MYSQL_USER, password=MYSQL_PASSWORD, port=MYSQL_PORT,database=MYSQL_DATABASE)