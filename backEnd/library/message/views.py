from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from message import models
from datetime import datetime
import time
import json

# Create your views here.

#登录注册模块Login
#登录 LoginServlet
def LoginServlet(request):
    dic = {}
    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        userID = received_json_data['userID']
        userPassword = received_json_data['userPassword']
        print(userID)
        print(userPassword)
        # 查询 userID
        userEX = models.User.objects.filter(userID = userID)
        if userEX.exists() == 0 :
            dic['userID'] = "__ERROR__"
            dic['msg'] = "用户不存在"
            dic = json.dumps(dic)
            return HttpResponse(dic)
        # 获取 userID 对应信息
        userX = models.User.objects.get(userID = userID)
        if userX.userPassword != userPassword :
            print(userX.userPassword)
            dic['userID'] = "__ERROR__"
            dic['msg'] = "密码错误"
            dic = json.dumps(dic)
            return HttpResponse(dic)
        # 匹配成功
        dic['status'] = userX.status
        dic['msg'] = ""
        dic = json.dumps(dic)
        return HttpResponse(dic)
    else :
        dic['userID'] = "__ERROR__"
        dic['msg'] = "请求错误"
        dic = json.dumps(dic)
        return HttpResponse(dic)