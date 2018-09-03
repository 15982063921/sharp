
from django.shortcuts import  HttpResponse
from django.shortcuts import render,render_to_response
from cmdb.models import User
#from cmdb import models

# Create your views here.
userinfo=[]
def index(request):

    if request.method=='POST':
        username = request.POST.get("username",None)
        password = request.POST.get("password", None)
        #添加到数据库
        user = User()
        user.name = username
        user.pwd = password
        user.save()
        #models.UserInfo.objects.create(user=username,pwd=password)
        #从数据库读取所有数据
        #user_list = models.UserInfo.objects.all()
        userinfolist = User.objects.all()
        return render_to_response('index.html', {'data': userinfolist,'da': 'uhh'})
    return render(request,"index.html")
    #return render_to_response('index.html', {'data': user_list})
def delete(request):
    sid=request.POST.get('sid',None)
    User.objects.filter(sid=request.GET.get('sid', None)).first().delete()
    userinfolist = User.objects.all()
    return render_to_response('index.html', {'data': userinfolist,'da': 'uhh'})