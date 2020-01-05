from django.contrib import admin
from app2.models import *
import datetime
class saleAdmin(admin.ModelAdmin):
    list_display = ["itemname","day","time1"]
# Register your models here.
admin.site.register(sale,saleAdmin)