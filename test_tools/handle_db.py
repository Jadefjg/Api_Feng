
""" 操作数据库 """

import psycopg2
from test_tools.handle_ini import conf

class HandleDb:

    def __init__(self):
        self.conn = psycopg2.connect(
                host = conf.get("postgresql","db_host"),
                port = conf.get("postgresql","db_port"),
                user = conf.get("postgresql","db_user"),
                password = conf.get("postgresql", "db_password"),
                database = conf.get("postgresql","db_name"),
        )
        self.cur = self.conn.cursor()

    # 1、查询返回数据列表 ===》 list
    def get_db_all_value_list(self,sql):
        result_list = []
        self.cur.execute(sql)
        result = self.cur.fetchall()
        #print(result)
        for val in result:
            for key,value in val.items():
                result_list.append(value)
        return result_list

    # 2、查询返回全部数据 ===》多个元组
    def get_db_all_data(self,sql):
        self.cur.execute(sql)
        res = self.cur.fetchall()
        return res

    def close(self):
        self.cur.close()
        self.conn.close()


postgresql = HandleDb()


# if __name__ == "__main__":
#     A = HandleDb()
#     sql = "select * from shang_join_information"
#     A.get_db_all_data(sql)




# self.conn = db.connect()  # 建立数据库连接
# cur = self.conn.cursor()  # 通过获取到的数据库连接conn下的cursor()方法来创建游标。
# cur.execute()             # 过游标cur 操作execute()方法可以写入纯sql语句。通过execute()方法中写如sql语句来对数据进行操作。
# cur.commit()              # conn.commit()方法在提交事物，在向数据库插入(或update)一条数据时必须要有这个方法，否则数据不会被真正的插入。
# cur.rollback()            # 发生错误时候回滚
# cur.fetchone()            # 返回单个元组
# cur.fetchall()            # 返回多个元组
# cur.fetchmany()           #
# cur.close()               # cur.close() 关闭游标
# conn.close()              # conn.close()关闭数据库连接



