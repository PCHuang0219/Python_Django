import MySQLdb
from rest_framework.response import Response
from rest_framework import status

class Sonic_Image_Version_Database():
    def __init__(self):
        self.conn = MySQLdb.connect(host="192.168.40.82",user="username", passwd="password",db="forum", charset="utf8") 
        self.cursor = self.conn.cursor()  

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def get_Image_Version_data(self):
        sql = "SELECT * FROM sonic_image_version"
        self.cursor.execute(sql)  
        results = self.cursor.fetchall()
        self.conn.commit()
        return  Response({"data":results},status=status.HTTP_200_OK)