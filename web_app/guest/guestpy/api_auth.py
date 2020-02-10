from django.contrib import  auth as django_auth
import base64

# 用户认证
"""user_auth函数的处理珠岙过程是提取出用户认证数据并判断其正确性"""
def user_auth(request):
# request.META是一个python字典，包含了本次http请求的Header信息
# HTTP_AUTHORIZATION用于获取HTTP认证数据，若为空则得到一个空的bytes对象
# 若用户传输的认证数据为admin/admin123456则会得到：Basic  YWRtaW46YWRtaW4xMjM0NTY=
    get_http_auth = request.META.get('HTTP_AUTHORIZATION',b'')
# 用split方法将其拆成两段
    auth = get_http_auth.split()
    try:
        # 提取list中的加密串，通过base64对其进行解码
        auth_parts = base64.b64decode(auth[1]).decode('utf-8').partition(':')
    except IndexError:
        return "null"
# 去除对应的username和password，对其进行验证
    username,password = auth_parts[0],auth_parts[2]
    user = django_auth.authenticate(username=username,password=password)
    if user is not None:
        django_auth.login(request,user)
        return "success"
    else:
        return "fail"

# 查询发布会接口，增加用户认证
def get_event_list(request):
    auth_result = user_auth(request)#调用认证函数
    if auth_result == "null":
        return JsonResponse({'status':10011,'message':'user auth null'})
    if auth_result == "fail":
        return JsonResponse({'status': 10012, 'message': 'user auth fail'})
    eid = request.GET.get("eid","")
    name = request.GET.get("name","")
    """略"""

import time,hashlib
# 用户签名+时间戳
def user_sign(request):
    if request.method == 'POST':
        client_time = request.POST.get('time','')
        client_sign = request.POST.get('sign','')
    else:
        return  "error"

    if client_time =='' or client_sign =='':
        return  "sign null"

    # 服务器时间
    now_time = time.time()
    server_time = str(now_time).split('.')[0]
    #获取时间差
    time_difference = int(server_time) - int(client_time)
    if time_difference >= 60:
        return "timeout"
    # 签名检查
    md5 = hashlib.md5()
    sign_str = client_time + "&Guest-Bugmaster"
    sign_bytes_utf8 = sign_str.encode(encoding="utf-8")
    md5.update(sign_bytes_utf8)
    server_sign = md5.haxdigest()

    if server_sign != client_sign:
        return "sign fail"
    else:
        return "sign success"
# 添加发布会接口--增加签名+时间戳
def add_event(request):
    sign_result =user_sign(request)
    if sign_result == "error":
        return JsonResponse({'status': 10011, 'message': 'request error'})
    elif sign_result =="sign null":
        return JsonResponse({'status': 10012, 'message': 'user sign null'})
    elif sign_result == "timeout":
        return JsonResponse({'status': 10013, 'message': 'user sign timeout'})
    elif sign_result == "sign fail":
        return  JsonResponse({'status': 10014, 'message': 'user sign fail'})
# AES加密接口开发
from Crypto.Cipher import AES
BS = 16
unpad = lambda s:s[0: - ord(s[-1])]
def encryptBase64(self, src):
    return base64.urlsafe_b64encode(src)
def decryptAES(src,key):
    iv = b'1172311105789011'
    cryptor = AES.new(key,AES.MODE_CBC,iv)
    text = cryptor.decrypt(src).decode()
    return unpad(text)
def aes_encryption(request):
    app_key = 'W7v4D60fds2Cmk2U'
    if request.method == "POST":
        data = request.POST.get("data","")
    else:
        return "error"
    # 解密
    decode = decryptAES(data,app_key)
    # 转换为字典
    dict_data = json.loads(decode)
    return dict_data
# AES加密测试用例
from Crypto.Cipher import AES
import base64
import requests
import unittest
import json
class AESTest(unittest.TestCase):
    def setup(self):
        BS = 16
        self.pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
        self.base_url = "http://127.0.0.1:8000/api/sec_get_guest_list/"
        self.app_key = 'W7v4D60fds2Cmk2U'
    def encryptBase64(self,src):
        return base64.urlsafe_b64encode(src)
    def encryptAES(self,src,key):
        """生成AES密文"""
        iv = b'1172311105789011'
        cryptor = AES.new(key,AES.MODE_CBC,iv)
        ciphertext = cryptor.encrypt(self.pad(src))
        return self.encryptBase64(ciphertext)
    def test_aes_interface(self):
        pyload = {'eid':'1','phone':'18011001100'}
        encoded = self.encryptAES(json.dumps(pyload),self.app_key).decode()
        r =requests.post(self.base_url,data={'data':encoded})
        result =r.json()
        self.assertEqual(result['status'],200)
        self.assertEqual(result['message'],"success")
if __name__ == '__main__':
    unittest.main()
