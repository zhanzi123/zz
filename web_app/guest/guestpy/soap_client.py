from suds.client import Client
from suds.xsd.doctor import ImportDoctor,Import
"""电话号码归属地查询"""
# url = 'http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl'
# client = Client(url)
# # print(client)
# result = client.service.getMobileCodeInfo('15972823388')
# print(result)
"""天气查询接口"""
url = "http://www.webxml.com.cn/WebServices/WeatherWebService.asmx?wsdl"
# client = Client(url)
imp = Import("http://www.w3.org/2001/XMLSchema",
             location="http://www.w3.org/2001/XMLSchema.xsd")
imp.filter.add("http://WebXml.com.cn/")
client = Client(url,plugins=[ImportDoctor(imp)])
# print(client)
result = client.service.getWeatherbyCityName("北京")
print(result)