from django.contrib import admin
from .models import Slider
from .models import Team , About
from django.utils.html import format_html

# Register your models here.
class TeamAdmin(admin.ModelAdmin):

    def myphoto(self, object):
        return format_html('<img src="{}" width= "40"/>'.format(object.photo.url))
    list_display = ('id','myphoto','first_name','Role','created_date')
    list_display_links = ('first_name','id')
    search_fields = ('first_name','Role')
    list_filter = ('Role',)
class Slider_Edit(admin.ModelAdmin):
    def myphoto(self, object):
        return format_html('<img src="{}" width= "40"/>'.format(object.photo.url))
    list_display = ('headline','button_text','myphoto','photo')

admin.site.register(Slider,Slider_Edit)
admin.site.register(Team,TeamAdmin)
admin.site.register(About)