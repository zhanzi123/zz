from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.set_window_size(800,600)
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()

'''通过javascript设置浏览器的滚动条位置'''
js = "window.scrollTo(100,500);"
driver.execute_script(js)
#将页面上下滚动、左右滚动值设置最大值为10000，然后再滚动到想滚动的位置
driver.execute_script("var action=document.documentElement.scrollTop=10000;")
driver.execute_script("var action=document.documentElement.scrollLeft=10000;")
time.sleep(2)
driver.execute_script("window.scrollTo(10000,10000)")

'''调用javascript在textarea属性输入框中输入文字'''
text = " input text"
js = "documnent.getElementById('id').value='" + text + "';"
driver.execute_script(js)
