import os
import configparser    # python3

cur_path = os.path.dirname(os.path.realpath(__file__))
configPath = os.path.join(cur_path, "cfg.ini")      # 绝对路径


class HandleIni:

    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.conf.read(configPath, "utf-8")

    def host_url(self):
        host_url = self.conf.get('host','host_url')
        # rint(host_url)
        return host_url

    def send_email(self):
        smtp_server = self.conf.get('email', 'smtp_server')
        sender = self.conf.get('email', 'sender')
        psw = self.conf.get('email', 'psw')
        receiver = self.conf.get('email', 'receiver')
        port = self.get('email', 'port')

        return smtp_server,sender,psw,receiver,port

    def mysql_sql(self):
        pass

    def postgresql_sql(self):
        pass

a = HandleIni()
print(a.host_url())