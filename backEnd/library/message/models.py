from django.db import models

# Create your models here.

#常量
MAX_LENTH_ID = 64
MAX_LENTH_PASSWORD = 64
MAX_LENTH_STRING = 64

# 建立数据库中的表格

# 用户登录信息
class User(models.Model):
    objects = models.Manager()
    userID = models.CharField(primary_key=True, max_length=MAX_LENTH_ID)
    userPassword = models.CharField(max_length=MAX_LENTH_PASSWORD)
    userGender = (( "男",'male'),( "女",'female'),) #性别
    userAge = models.IntegerField(blank=True,null=True) #年龄
    userDepartment = models.CharField(blank=True,null=True,max_length=MAX_LENTH_STRING) #院系
    userInBlacklist = models.IntegerField() # 默认0 (0 or 1)