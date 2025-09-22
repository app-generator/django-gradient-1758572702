# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    username = models.TextField(max_length=255, null=True, blank=True)
    password = models.TextField(max_length=255, null=True, blank=True)
    email = models.TextField(max_length=255, null=True, blank=True)
    registration_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Carbon_Items(models.Model):

    #__Carbon_Items_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)

    #__Carbon_Items_FIELDS__END

    class Meta:
        verbose_name        = _("Carbon_Items")
        verbose_name_plural = _("Carbon_Items")



#__MODELS__END
