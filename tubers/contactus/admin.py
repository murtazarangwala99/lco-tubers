from django.contrib import admin
from .models import Contactus
# Register your models here.
class ContactEdit(admin.ModelAdmin):
    list_display= ('full_name','subject','email')

admin.site.register(Contactus,ContactEdit)