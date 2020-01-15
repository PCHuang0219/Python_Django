import MySQLdb

class Initial_Database():
    def __init__(self):
        self.conn = MySQLdb.connect(host="127.0.0.1",user="root", passwd="5566",db="forum", charset="utf8") 
        self.cursor = self.conn.cursor()  
        #self.clear_table()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def clear_table(self):
        self.clear_User_Type_table()
        self.clear_User_Auth_table()

    def clear_User_Type_table(self):
        SQL="DELETE FROM sonic_user_type"
        self.cursor.execute(SQL) 
        if(not self.conn.commit()): 
            print("clear sonic_user_type table success")

    def clear_User_Auth_table(self):
        SQL="DELETE FROM auth_user"
        self.cursor.execute(SQL) 
        if(not self.conn.commit()): 
            print("clear auth_user table success")

    def initial_user_type_data(self,index_id=1,user_id=1,user_type_id=1):
        SQL='INSERT INTO sonic_user_type (`id`, `user_id`, `user_type_id`)\
            VALUES ("%s", "%s", "%s")'\
            %(index_id,user_id,user_type_id)    
        self.cursor.execute(SQL)  
        self.conn.commit()
    

initial_database = Initial_Database()
initial_database.initial_user_type_data()
initial_database.initial_user_type_data(2,2,2)







 
