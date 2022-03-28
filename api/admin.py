from django.contrib import admin
from api.models import Phone , Email_log , Student


class PhoneAdmin(admin.ModelAdmin):
    model = Phone
    list_display = ['phone_number' , 'user','country' , 'city']
    
admin.site.register(Phone, PhoneAdmin)


class EmailAdmin(admin.ModelAdmin):
    model = Email_log
    list_display = ['email' , 'subject']
    search_fields = ['email' , 'subject']
    list_filter = ['email' , 'subject']
    
admin.site.register(Email_log, EmailAdmin)

class StudentAdmin(admin.ModelAdmin):
    model = Student
    list_display = ['id' , 'name' , 'roll' , 'city' , 'passby']
    
admin.site.register(Student, StudentAdmin)

