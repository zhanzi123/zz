import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("wwww.url.com")
time.sleep(2)
driver.switch_to.frame("iframe")
driver.find_element_by_id("appDate").click()

#定位要滑动的年、月、日
dwwos = driver.find_element_by_class_name("dwwwo")
year = dwwos[0]
month = dwwos[1]
day = dwwos[2]

action = webdriver.TouchActions(driver)
action.scroll_from_element(year,0,5).perform()
action.scroll_from_element(month,0,30).perform()
action.scroll_from_element(day,0,30).perform()

"""这里使用TouchActions类中的scroll_from_element()方法滑动元素，参数如下：
on_element:滑动的元素
xoffset:x坐标距离
yoffset:y坐标距离
"""