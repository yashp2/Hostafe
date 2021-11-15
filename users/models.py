from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

class extendeduser(models.Model):

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=10,null=True,default=" ")
    last_name = models.CharField(max_length=12,null=True,default=" ")
    
    user = models.OneToOneField(User,on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.user.username}'