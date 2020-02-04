import requests
# r = requests.get('https://api.github.com/user',auth=('zhanzi123','zzy950714'))
#
# print(r.status_code)
# print(r.headers['Content-Type'])
# print(r.encoding)
# print(r.text)
# print(r.json())

# url = "https://127.0.0.1:8000/api/get_event_list/"
# r = requests.get(url,params={'end':'1'})
# result = r.json()
# print(result)

# r= requests.get("http://127.0.0.1:5000/")
# result = r.json()
# print(result)
# print(result['code'])
# print(result['message'])
# print(r.status_code)
# print(r.headers)
# print(r.headers['Content-Type'])
# print(r.encoding)
# print(r.text)

# name = "zhanzi"
# r = requests.get("http://127.0.0.1:5000/user/"+name)
# # print(r.json())
# if name in r.json()['message']:
#     print('pass')
# else:
#     print('false')

# uid = '1'
# r = requests.get("http://127.0.0.1:5000/id/"+uid)
# print(r.json())

'''一般get请求'''
'''方法一'''
# payload = {"q":"selenium"}
# r = requests.get("http://127.0.0.1:5000/search/",params=payload)
# print(r.json())
'''方法二'''
# r=requests.get("http://127.0.0.1:5000/search/?q=selenium")
# print(r.json())

'''post请求'''
'''参数类型为：from-data/x-www-from-urlencode'''
# payload = {'username':'admin','password':'a123456'}
# r = requests.post("http://127.0.0.1:5000/login",data=payload)
# print(r.json())
# payload = {'username':'','password':'a123456'}
# r = requests.post("http://127.0.0.1:5000/login",data=payload)
# print(r.json())
# payload = {'username':'admin','password':''}
# r = requests.post("http://127.0.0.1:5000/login",data=payload)
# print(r.json())
# payload = {'username':'admin','password':'123456'}
# r = requests.post("http://127.0.0.1:5000/login",data=payload)
# print(r.json())
# payload = {'username':''}
# r = requests.post("http://127.0.0.1:5000/login",data=payload)
# print(r.json())
'''post请求'''
'''参数类型为：json'''
# payload = {'name':'jack','age':'22','height':177}
# r = requests.post("http://127.0.0.1:5000/add_user",json=payload)
# print(r.json())
# payload = {'name':123,'age':123,'height':'xcv'}
# r = requests.post("http://127.0.0.1:5000/add_user",data=payload)
# print(r.json())
# payload = {'name':'admin','age':'22'}
# r = requests.post("http://127.0.0.1:5000/add_user",json=payload)
# print(r.json())
# payload = {'age':'22','height':177}
# r = requests.post("http://127.0.0.1:5000/add_user",json=payload)
# print(r.json())
# payload = {'name':'jack','age':'','height':177}
# r = requests.post("http://127.0.0.1:5000/add_user",json=payload)
# print(r.json())
'''post请求'''
'''带header的接口'''
# header = {"Content-Type": "application/json",
#             "token": "3d80caXELzU1aWmHwxl0TzW7jtterObm8l5EeAfipnhyaKmhFl8KdhFRvy4"}
# r = requests.post("http://127.0.0.1:5000/header", headers=header)
# print(r.json())
# r = requests.post("http://127.0.0.1:5000/header")
# print(r.json())
# header = {}
# r = requests.post("http://127.0.0.1:5000/header",headers=header)
# print(r.json())
'''post请求'''
'''上传文件的接口'''
# files = {'file':open(r'D:\log.txt','rb')}
# r = requests.post("http://127.0.0.1:5000/upload", files=files)
# print(r.json())

'''同一个url，根据方法实现不同功能'''
'''get请求一般用来获取该接口'''
# r = requests.get("http://127.0.0.1:5000/phone/0")
# print(r.json())
# r = requests.get("http://127.0.0.1:5000/phone/1")
# print(r.json())
# for i in range(0,10):
#     r = requests.get("http://127.0.0.1:5000/phone/"+str(i))
#     print(r.json()['message'],end='--->')
#     if 'success' in str(r.json()):
#         print("存在编号为"+str(i)+"的手机",end='\n')
#     else:
#         print("不存在编号为"+str(i)+"的手机",end='\n')
'''put请求一般作为更新数据接口'''
# data = {"name":"华为手机","price":"3999"}
# r = requests.get("http://127.0.0.1:5000/phone/0",data=data)
# print(r.json())
# r = requests.get("http://127.0.0.1:5000/phone/1",data=data)
# print(r.json())
'''delete请求一般用作删除数据接口'''
# r = requests.delete('http://127.0.0.1:5000/phone/1')
# print(r.json())
# r = requests.delete('http://127.0.0.1:5000/phone/0')
# print(r.json())
'''通过session记录登录状态'''
# s = requests.Session()
# r = s.post("http://127.0.0.1:5000/user_login", data={"username": "jack", "password": "123"})
# print(r.json())
# r2 = requests.get("http://127.0.0.1:5000/user_data")
# print(r2.json())
# r3 = s.get("http://127.0.0.1:5000/user_data")
# print(r3.json())
'''依赖接口的调用'''
# #获取活动id
# r = requests.get("http://127.0.0.1:5000/get_activity")
# print(r.json())
# acticity_id = r.json()["data"]["id"]
# print(acticity_id)
# #获取用户id
# r = requests.get("http://127.0.0.1:5000/get_user")
# print(r.json())
# user_id = r.json()["data"]["id"]
# print(user_id)
# #调用获取抽奖号码接口
# data = {"aid":acticity_id,"uid":user_id}
# r = requests.post("http://127.0.0.1:5000/lucky_number", data=data)
# print(r.json())


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://note.youdao.com/web/#/file/SVR177DE7B396A54CFFA1A82B1416DC9CB4/default/WEBd6a4f4e423ac93cd21f32184d0081f18/')
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[1]/div[1]/span").click()
time.sleep(1)
driver.find_element_by_css_selector('#switcher_plogin').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="u"]').send_keys('1025042582')
driver.find_element_by_xpath('//*[@id="p"]').send_keys('zhanzi19950714')
driver.find_element_by_xpath('//*[@id="p"]').submit()
time.sleep(1)
a = ActionChains(driver)