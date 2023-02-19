import rsa
import base64
from time import time


class HandleSign:

    publickey = ""

    @classmethod
    def encrypt(cls,msg):
        msg = msg.encode("utf-8")
        pub_key = cls.publickey.encode("utf-8")
        public_key_obj = rsa.PublicKey.load_pkcs1_openssl_pem(pub_key)  # 创建 PublicKey 对象
        cryto_msg = rsa.encrypt(msg,public_key_obj)                     # 生成加密文本
        cipher_base64 = base64.b64encode(cryto_msg)                     # 将加密文本转化为 base64 编码
        result = cipher_base64.decode()                                 # 将字节类型的 base64 编码转化为字符串类型
        return result

    @classmethod
    def generate_sign(cls,token):
        timestamp = int(time())     # 获取当前的时间戳
        prefix_50_token = token[:50]
        message = prefix_50_token + str(timestamp)  # 将 token 前50位与时间戳字符串进行拼接
        sign = cls.encrypt(message)                 # 生成sign
        return {"timestamp":timestamp,"sign":sign}

if __name__== '__main__':
    # token = ""
    # cryto_info = HandleSign.generate_sign(token)
    # print(cryto_info)
    # s = "123456"
    # print(HandleSign.dencrypt('123456'))
    pass