import email
from enum import unique
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
    
    
    
    
    
    