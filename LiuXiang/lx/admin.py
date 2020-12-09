from django.contrib import admin
from .models import Idsp, Liuxiangpinzhong

# Register your models here.


# @admin.register(Idsp)
# class idsp(admin.ModelAdmin):
#     list_display = ('spid', 'type')
#     list_editable = ('type',)
#     search_fields = ('spid',)
#     list_per_page = 15


@admin.register(Liuxiangpinzhong)
class idsp(admin.ModelAdmin):
    list_display = ('spbh_c', 'liuxiangid', 'shifoushengxiao')
    list_editable = ('liuxiangid', 'shifoushengxiao')
    search_fields = ('spbh_c',)
    list_per_page = 15



admin.site.site_header = '流向管理'
admin.site.site_title = 'Django'