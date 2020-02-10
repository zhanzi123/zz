from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event
# Create your views here.
def index(request):
    return HttpResponse("hahaha")
    
def zhanzi(request):
    return HttpResponse("zhanzi NB!")
    
def login(request):
    return render(request,"index.html")
    
#登录动作
def login_action(request):
    if request.method == "POST":
        username = request.POST.get("username","")
        password = request.POST.get("password","")
        user = auth.authenticate(username=username,password=password)
        # if username == "admin" and password == "admin123":
        if user is not None:
            auth.login(request,user)#登录
            response =  HttpResponseRedirect("/event_manage/")
            # response.set_cookie('user',username,3600)#添加浏览器cookie，将传过来的username与user字段匹配，市场3600s
            request.session['user'] = username #将session信息记录到浏览器
            return response
        else:
            return render(request,"index.html",{'error':'账号或密码错误!'})
@login_required
def event_manage(request):
    event_list = Event.objects.all()
    # username = request.COOKIES.get('user','')#读取浏览器cookie，默认为空
    username =request.session.get('user','')#读取浏览器session，默认为空
    return render(request,"event_manage.html",{"user":username,
                                               "events":event_list})