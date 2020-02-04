from poium import Page,PageElement
from selenium import webdriver
from web.pageobject import Baidusearch
import time
driver = webdriver.Chrome()
# driver = webdriver.Firefox()
page = Baidusearch(driver)
page.get('https://www.baidu.com')
driver.maximize_window()
# page.maximize_window()

# page.serchinput.sendkeys('poium')
# page.serchbutton.click()
page.search_input.send_keys('poium')
page.search_button.click()
time.sleep(1.5)
# driver.quit()