# for m in range(1,10):
#     for n in range(1,m+1):
#         print("%d*%d=%d"%(m,n,m*n),end=" ")
#     print()
#
# for m in range(1,10):
#     for n in range(1,m+1):
#         print("{}*{}={}".format(m,n,m*n),end=" ")
#     print()

# def sub(name,age):
#     """
#     这是说明文档
#     :param name: 传入一个名字
#     :param age: 传入一个年龄
#     :return: 打印出自我介绍
#     """
#     print("我的名字是" + name )
#     print(age)
#     pass
#
# sub("zhanzi",24)
# print(sub.__doc__)

# # 以下是参数配置信息，一般情况下配置这些即可
# from appium import webdriver
# desired_caps = {
#         'platformName': 'Android',  # 系统
#         'platformVersion': '9.0.',  # 版本号
#         'deviceName': 'b1e42155',  # 设备号 可以参数化
#         'appPackage': 'com.miui.calculator',  # 包名
#         'appActivity': 'com.miui.calculator.cal.CalculatorActivity#0',  # 启动名
#         'unicodeKeyboard': True,  # 允许输入中文
#         'resetKeyboard': True,
#         'autoAcceptAlerts': True,  # 默认选择接受弹窗的条款，有些app启动的时候，会有一些权限的弹窗
#         'reuse': 3,
#         'noReset': True,  # 每次appium对app进行操作，为了不保存修改数据和app设置的内容而不影响下次使用，需要设置为true
#         'automationName':"UiAutomator2",
#         'chromeOptions':
#                     {
#                      'androidProcess': 'com.tencent.mm:tools',
#                       'args': ['--no-sandbox']
#                    }
#  }
#
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


from appium import webdriver
from time import sleep


CAPS = {
    "deviceName": " b1e42155",
    # "automationName": "UiAutomator2",
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "appPackage": "com.tencent.mobileqq",
    "appActivity": "com.tencent.mobileqq.activity.SplashActivity",
    "noReset": True,
    "unicodeKeyboard": True,
    "resetKeyboard": True,
    "customFindModules": {"ai": "test-ai-classifier"},
    "testaiConfidenceThreshold": 0.1,
    "shouldUseCompactResponses": False,
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', CAPS)
sleep(2)
driver.find_element_by_id('com.tencent.mobileqq:id/et_search_keyword').click()
sleep(1)
driver.find_element_by_id('com.tencent.mobileqq:id/et_search_keyword').send_keys('湛子')
sleep(2)
driver.find_element_by_class_name('android.widget.FrameLayout').click()

sleep(1)
driver.find_element_by_class_name('android.widget.ImageView').click()      #有问题?
sleep(5)

driver.quit()