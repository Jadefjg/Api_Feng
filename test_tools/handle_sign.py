import rsa
import base64
from time import time

"""
    1、编码需要加密明文
        msg.encode('utf-8)
    2、创建公钥对象
        public_key_obj = rsa.PublicKey.load_plcs1_openssl_pem(pub_key)
    3、通过秘钥生成密文
        cryto_msg = rsa.encrypt(msg,public_key_obj)
    4、将加密文本转化为 base64 编码
        cipher_base64 = base64.b64encode(cryto_msg)
    5、将第四步得到的字节类型的 base64 编码转化为字符串类型
        cipher_base64.decode()
"""


class HandleSign:

    publickey = ""

    @classmethod
    def encrypt(cls,msg):
        """
            非对称加密
            :param msg: 待加密字符串或者字节
            :return: 加密后密文
        """
        msg = msg.encode("utf-8")
        pub_key = cls.publickey.encode("utf-8")
        public_key_obj = rsa.PublicKey.load_pkcs1_openssl_pem(pub_key)  # 创建 PublicKey 对象
        cryto_msg = rsa.encrypt(msg,public_key_obj)                     # 生成加密文本
        cipher_base64 = base64.b64encode(cryto_msg)                     # 将加密文本转化为 base64 编码
        result = cipher_base64.decode()                                 # 将字节类型的 base64 编码转化为字符串类型
        return result

    @classmethod
    def generate_sign(cls,token):
        """
            生成sign，对外使用
            :param timestamp: 当前秒级时间戳, 为int类型
            :param token: token, 为str类型
            :return: 时间戳和sign组成的字典
        """
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