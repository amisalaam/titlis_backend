from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .manager import CustomUserManager

# Create your models here.

class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(_('username'),max_length=255)
    email = models.EmailField(_('email address'), unique=True,max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True,verbose_name=_('date joined'))
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = CustomUserManager()
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        
    def __str__(self):
        return self.email
    

    
    
    
    
