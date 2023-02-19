
"""
一、四要素
1、姓名
    name = fk.name()
2、身份证
    card = fk.ssn()
3、手机号(停掉发短信的功能)
    phone = fk.phone_number()
4、银行卡
    card_number = fk.credit_card_number()

二、个人信息
1、地址(带邮编)
    addr = fk.address()
2、公司名称
    company = fk.company()
3、职位名称
    job = fk.job()
4、邮箱
    email = fk.email()
5、城市
    city = fk.city()
6、国家
    country = fk.country()
7、省份
    pro = fk.province()
8、生成完整的个人信息
    persion = fk.simple_profile()
    per = fk.profile()


三、文本类  
1、生成英文字符串
pystring = fk.pystr()
2、词语
word = fk.word()
3、文章
text = fk.text()
4、随机数
randon_num = fk.random_int(min=100,max=999)

四、时间类
当前时间
1、年  1970  -- 现在
year = fk.year()

2、月 
month = fk.month()

3、格式：年-月-日，1970 -- 现在
date = fk.date()

4、当前年：年-月-日
now = fk.date_this_year()

5、年-月-日 时:分:秒
this_time = fk.date_time()

6、指定时间范围
当前年：年-月-日
y:年  m：月
res1 = fk.date_between(start_date="-1y",end_date ="today" )

年-月-日 时:分:秒
# y:年  m：月 
res2 = fk.date_time_between(start_date="-3y",end_date ="-1y" )

7、未来时间
当前年：年-月-日
future1= fk.future_date()
年-月-日 时:分:秒
future2=fk.future_datetime()


五、高级用法
1、生成的数据不重复
name_list = [fk.unique.name() for i in range(10)]

2、数据共享（通过seed方法保持数据一致）
from faker import Faker
class Test:
    def __init__(self):
        self.fk = Faker(locale="zh-CN")

    def test01(self):
        Faker.seed(11111)
        print(self.fk.name())

    def test02(self):
        Faker.seed(11111)
        print(self.fk.name())
"""


from faker import Faker

fk = Faker(locale="zh-CN")


this_name = fk.name()

name_list = [fk.unique.name() for i in range(10)]

num_list = [i for i in range(10)]



future1= fk.future_date()
future2=fk.future_datetime()
time_zone = fk.timezone()



# y:年  m：月
res2 = fk.date_time_between(start_date="-3y",end_date ="-1y" )

# y:年  m：月
# res1 = fk.date_between(start_date="-1y",end_date ="today" )



# 年-月-日 时:分:秒
this_time = fk.date_time()

# 当前年：年-月-日
now = fk.date_this_year()

#格式：年-月-日
date = fk.date()

# 年  1970  -- 现在
year = fk.year()
month = fk.month()






# 随机数
randon_num = fk.random_int(min=100,max=999)




# 根据百家姓随机拼接中文进行生成，
# 姓名
name = fk.name()

# 身份证
card = fk.ssn()

# 手机号
phone = fk.phone_number()

# 银行卡
card_number = fk.credit_card_number()

# 地址
addr = fk.address()

# 公司名称
company = fk.company()


# 邮箱
email = fk.email()

job = fk.job()

# 城市
city = fk.city()

# 国家
country = fk.country()

# 省
pro = fk.province()


# 简单的人物信息
persion = fk.simple_profile()
per = fk.profile()


# 生成英文字符串
pystring = fk.pystr()

# 生成词语
word = fk.word()

text = fk.text()






