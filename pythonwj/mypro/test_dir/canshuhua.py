import seldom
from seldom import ddt
from selenium import webdriver
import unittest
from parameterized import parameterized, parameterized_class
# ...
@parameterized([
    ("a"),
    ("b"),
    ("c"),
    ("d"),
])



def search(a):
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    driver.find_element_by_id("kw").send_keys(a)
    driver.find_element_by_css_selector("#su").click()
    driver.close()
#
# class BaiduTest(unittest.TestCase):
#
#     def test_A(self,x):
#         search(x)








# class BaiduTest(seldom.TestCase):
#
#     @ddt.data([
#         ('seldom'),
#         ('selenium'),
#         ('unittest'),
#     ])
    # def test_baidu(self,x):
    #     """
    #      used parameterized test
    #     :param name: case name
    #     :param keyword: search keyword
    #     """
    #     self.search(x)
    #     search(x)

    # def search(self,b):
        # self.open("https://www.baidu.com")
        # self.type(id_="kw", text=b)
        # self.click(css="#su")
        # self.assertTitle(b+"_百度搜索")
        # self.close()


