from django.db import models
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):

    def _create_user(self, phone_number, password,
                     is_provider,is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not phone_number:
            raise ValueError('The given phone_number must be set')
        if is_provider is None:
          is_provider = False
        user = self.model(phone_number=phone_number,
                          is_provider=is_provider,is_staff=is_staff,is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, password=None, is_provider=None, **extra_fields):
        return self._create_user(phone_number, password, is_provider, False,False,
                                 **extra_fields)

    def create_superuser(self, phone_number, password, **extra_fields):
        return self._create_user(phone_number, password, True, True,True,
                                 **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=254, unique=True)
    is_provider = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)


    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()


class Contact(models.Model):
  first_name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)
  phone_number = models.CharField(max_length=200)


  def __str__(self):
    return self.first_name + ' ' + self.last_name

