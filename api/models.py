from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User


class Phone(models.Model):
    phone_number = models.IntegerField(
        _("Phone Number"),
        unique=True,
        blank=False,
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL , blank=True,null=True)
    country = models.CharField(_("Country"),max_length=50, blank=True, null=True)
    city = models.CharField(_("City"),max_length=50, blank=True, null=True)
    address = models.CharField(_("Address"),max_length=250, blank=True, null=True)
    email = models.CharField(_("Email"),max_length=250, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
    
    def __str__(self):
        return str(self.phone_number)
    
class Email_log(models.Model):
    email = models.CharField(_("Receiver Email"),max_length=256 , blank=False, null=False)
    subject = models.CharField(_("Subject"),max_length=256,blank=False, null=False)
    body = models.CharField(_("Body"),max_length=1500)
    # is_sent = models.BooleanField(default=False , editable=False)
    
    def __str__(self):
        return "Email(Email _id : {} , Message Subject : {} )".format(self.email, self.subject)
    
    
class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    city = models.CharField(max_length=50)
    passby = models.CharField(max_length=50)
    
    
    
    
    
    