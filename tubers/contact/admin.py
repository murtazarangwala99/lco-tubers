from django.contrib import admin
from . models import Detail
# Register your models here.
class Edit_detail(admin.ModelAdmin):
    list_display = ('mail','call','fb_link')
admin.site.register(Detail,Edit_detail)