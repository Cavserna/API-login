from django.db import models

from django.contrib.auth.models import(AbstractBaseUser,PermissionsMixin,BaseUserManager)

# Create your models here.

class UseManager(BaseUserManager):
    def create_user(self, name, password, rol, branch):
        if not name:
            raise ValueError("No ingresó un nombre.")
        user = self.model(name=name, rol=rol, branch=branch)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, name, password):
        user = self.model(name=name)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user
    
        
class User(AbstractBaseUser,PermissionsMixin):
    
    name = models.CharField(max_length=250,unique=True)
    rol=models.CharField(max_length=50)
    branch= models.CharField(max_length=50)
    is_staff= models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    
    
    objects= UseManager()
    
    USERNAME_FIELD = "name"

