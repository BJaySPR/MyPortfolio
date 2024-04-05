from django.contrib import admin
from .models import Send_messate
# Register your models here.
@admin.register(Send_messate)
class Send_messateAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','message']
