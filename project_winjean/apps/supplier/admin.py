from django.contrib import admin

# Register your models here.
from django.http import HttpResponseRedirect
from supplier import models


@admin.register(models.Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'status', 'create_time']
    search_fields = ['name', 'gender', 'create_time']
    # list_display_links = ('name', )
    # list_editable = ('gender', )
    list_per_page = 8
    # save_as_continue = False

    actions = ['custom_button']

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return True

    def custom_button(self, request, queryset):
        # models.Supplier.objects.(name='111')
        # print(request)
        # return HttpResponseRedirect("../")
        # return True
        pass

    # 显示的文本，与django admin一致
    custom_button.short_description = '测试按钮'
    # icon，参考element-ui icon与https://fontawesome.com
    custom_button.icon = 'el-icon-message-solid'

    # 指定element-ui的按钮类型，参考https://element.eleme.cn/#/zh-CN/component/button
    custom_button.type = 'danger'

    # 给按钮追加自定义的颜色
    custom_button.style = 'color:black;'
    custom_button.confirm = '你是否执意要点击这个按钮？'

    custom_button.action_type = 0
    custom_button.action_url = '/admin/supplier/supplier/111'
