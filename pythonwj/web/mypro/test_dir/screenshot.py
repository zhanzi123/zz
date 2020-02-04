from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.save_screenshot("C:\baidu.png")

driver.quit()