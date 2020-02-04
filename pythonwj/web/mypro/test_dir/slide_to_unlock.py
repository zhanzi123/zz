from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException
import time
driver =webdriver.Chrome()
driver.get("https://www.bilibili.com/")
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="bili-header-m"]/div[1]/div[3]/div[2]/div[1]/ul/li[1]/a').click()
time.sleep(1)
driver.find_element_by_css_selector("#login-username").send_keys("13647230209")
driver.find_element_by_css_selector("#login-passwd").send_keys("zzy950714")
driver.find_element_by_link_text("登录").click()
time.sleep(1)

#定位到滑块
slider = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[6]/div/div[1]/div[2]/div[2]")
action = ActionChains(driver)

action.click_and_hold(slider).perform()

'''这种适用于划到顶会有alert弹窗的'''
'''如果是那种滑块拼图的，需要适当改造，目前那种验证码只能在循环中试出来，最好的办法是让开发去掉'''
for index in range(200):
    try:
        action.move_by_offset(2,0).perform()
    except UnexpectedAlertPresentException:
        break
    action.reset_actions()
    time.sleep(1)

#打印警告框提示
success_text = driver.switch_to.alert.text
print(success_text)