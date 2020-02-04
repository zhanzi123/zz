import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.acfun.cn/")
driver.maximize_window()
time.sleep(2)
a = driver.find_element_by_xpath('//*[@id="main"]/section[3]/div[1]/div[1]/div[1]/figure[1]/a')
a.href = a.get_attribute('href')
print(a.href)
driver.get(a.href)

video = driver.find_element_by_xpath('//*[@id="ACFlashPlayer"]/div/div[1]/video')

#返回播放文件地址
url = driver.execute_script("return arguments[0].currentSrc;",video)
print(url)


'''acfun默认直接播放，所以先等播放一会儿再暂停，再播放，再暂停'''
#播放15s
time.sleep(15)
#暂停视频
print("sleep")
driver.execute_script("arguments[0].pause()",video)

time.sleep(3)
#播放视频
print('start')
driver.execute_script("arguments[0].play()",video)

time.sleep(3)
#暂停视频
print("sleep")
driver.execute_script("arguments[0].pause()",video)

'''JavaScript中有个内置对象叫做arguments，arguments包含函数调用的参数数组，[0]表示取对象的第一个值'''
'''currentSrc返回当前音频/视频的URL，弱国未设置音频视频，则返回空字符串'''
'''load()、play()、pause()控制视频的加载、播放和暂停'''