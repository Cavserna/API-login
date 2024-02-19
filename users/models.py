from django.db import models

from django.contrib.auth.models import(AbstractBaseUser,PermissionsMixin,BaseUserManager)

# Create your models here.

class UseManager(BaseUserManager):
    def create_user(self, nombre_usuario, contrasena, rol, sucursal):
        if not nombre_usuario:
            raise ValueError("No ingresó un nombre.")
        user = self.model(nombre_usuario=nombre_usuario, rol=rol, sucursal=sucursal)
        user.set_contrasena(contrasena)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, nombre_usuario, contrasena):
        user = self.model(nombre_usuario=nombre_usuario)
        user.set_contrasena(contrasena)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user






class User(AbstractBaseUser,PermissionsMixin):
    
    nombre_usuario = models.CharField(max_length=250,unique=True)
    rol=models.ForeignKey(Roles, on_delete=models.CASCADE)
    sucursal= models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    is_staff= models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    
    
    objects= UseManager()
    
    USERNAME_FIELD = "nombre_usuario"

