from django.contrib import admin
from api.models import Phone


class PhoneAdmin(admin.ModelAdmin):
    list_display = ['phone_number' , 'user','country' , 'city']
    
admin.site.register(Phone, PhoneAdmin)
