from selenium import webdriver

'''
webdriver操作cookie的方法：
get_cookies(): 获取所有cookie
get_cookie(name): 返回字典中key为"name“的cookie
add_cookie(cookie_dict): 添加cookie    如driver.add_cookie({'name':'key-aaaaaaaaa','value':'value-bbbbbbbbbbbbbb'})
delete_cookie(name,optionString): 删除名为openString的cookie
delete_all_cookies(): 删除所有cookie
'''


driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

#获取所有cookie信息并打印
cookie = driver.get_cookies()
print(cookie)

#添加cookie信息
driver.add_cookie({'name':'key-aaaaaaaaa','value':'value-bbbbbbbbbbbbbb'})

#遍历指定的cookies
for cookie in driver.get_cookies():
    print("%s -> %s" % (cookie['name'],cookie['value']))

driver.quit()