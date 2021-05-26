from django.db import models

# Create your models here.

#常量
MAX_LENTH_ID = 64
MAX_LENTH_PASSWORD = 64

# 建立数据库中的表格

# 用户登录信息
class User(models.Model):
    objects = models.Manager()
    userID = models.CharField(primary_key=True, max_length=MAX_LENTH_ID)
    userPassword = models.CharField(max_length=MAX_LENTH_PASSWORD)
