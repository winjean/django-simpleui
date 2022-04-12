from django.contrib import admin

# Register your models here.
from user.models import UserProfile

admin.site.site_header = '联成科技'

# 这个会在登陆的时候显示在浏览器标签页
admin.site.site_title = '管理系统'
admin.site.index_title = '项目管理首页'


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'telephone', 'email']
    search_fields = ['username', 'telephone', 'email']


admin.site.register(UserProfile, UserAdmin)
