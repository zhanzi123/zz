from appium import webdriver

'''定义运行环境'''
desired_caps = {
    'deviceName' : '3ec3afdd',
    'automationName' : 'appium',
    'platformName' : 'Android',
    'platformVersion' : '9',
    'appPackage' : 'com.baidu.tieba',
    'appActivity' : 'com.baidu.tieba.frs.FrsActivity#0',
}

driver = webdriver.Remote(command_executor='http://192.168.1.5:4723/wd/hub', desired_capabilities=desired_caps)

driver.find_element_by_id("com.android.caculator2:id/digit_1").click()
driver.find_element_by_id("com.android.caculator2:id/op_add").click()
driver.find_element_by_id("com.android.caculator2:id/digit_2").click()
driver.find_element_by_id("com.android.caculator2:id/eq").click()

driver.quit()
