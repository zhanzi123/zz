import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox import firefox_profile
import time

# fp = webdriver.FirefoxProfile()#调整火狐浏览器的设置
# fp.set_preference("browser.download.folderList",2)#设置为0使用浏览器默认路径，设置为2下载到指定目录
# # fp.set_preference("browser.download.dir",os.getcwd())
# fp.set_preference("browser.download.dir","D:\\")#设置默认路径
# # fp.set_preference("browser.helperApps.neverAsk.saveToDisk","binary/octet-stream")
# fp.set_preference("browser.helperApps.neverAsk.saveToDisk","application/octet-stream")
# driver = webdriver.Firefox(firefox_profile=fp)
# driver.get("https://hsdfas.fubangnet.com/#/user/login")
# time.sleep(1)
# driver.find_element_by_css_selector("div > div:nth-child(2) > .ant-btn.ant-btn-primary").click()
# time.sleep(2)

options = webdriver.ChromeOptions()
prefs = {
    "download.prompt_for_download": False,
    "plugins.always_open_pdf_externally": True,
    'profile.default_content_settings.popups': 0,
    'download.default_directory':'D:\\',
    'profile.default_content_setting_values.images': 2
}
options.add_experimental_option('prefs',prefs)
# options = webdriver.ChromeOptions()
# prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'd:\\'}
# options.add_experimental_option('prefs', prefs)


driver = webdriver.Chrome(options=options)
driver.get("https://hsdfas.fubangnet.com/#/user/login")
driver.find_element_by_css_selector("div > div:nth-child(2) > .ant-btn.ant-btn-primary").click()