#coding=utf8
from django.contrib import admin
from . import models
import pymysql
# Register your models here.


class EntryAdmin(admin.ModelAdmin):
    list_display = ['title','author','visiting','created_time','modifyed_time']


admin.site.register(models.Category)
admin.site.register(models.Tag)
admin.site.register(models.Entry,EntryAdmin)


pymysql.install_as_MySQLdb()
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'my_blog',        #数据库名字
        'USER': 'root',          #账号
        'PASSWORD': '123456',      #密码
        'HOST': '127.0.0.1',    #IP
        'PORT': '3306',                   #端口
    }
}