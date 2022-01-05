from django.contrib import admin
from .models import Hiretuber
# Register your models here.
class hiretuber_edit(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','email','tuber_name')
    list_display_links = ('first_name','id','last_name')
    search_fields = ('first_name','last_name')
    list_filter = ('city',)


admin.site.register(Hiretuber,hiretuber_edit)