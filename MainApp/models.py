from typing import NoReturn
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import BLANK_CHOICE_DASH
from django.db.models.fields.related import ForeignKey

# Create your models here.



# hostel name
# college name
# address
# radius
# gender
# contact number
# map link


# class Category(models.Model):
#     name=models.CharField(max_length=100)
#     def __str__(self):
#         return f'{self.name}'


class HostelInfo(models.Model):

    GENDER_CHOICES = (
        
            ("Male", "Male"),
            ("Female", "Female"),
            ("Coed","Coed")
            
        )
    # category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    college_name = models.CharField(max_length=200,null=True,default=" ")
    address = models.CharField(max_length=200,null=True,default=" ")
    radius= models.IntegerField(null=True,default=0)
    gender = models.CharField(max_length=12, choices=GENDER_CHOICES,null=True,default=" ")
    hostel_name = models.CharField(max_length=200,null=True,default=" ")
    cost_of_living= models.IntegerField(null=True,default=0)
    contact_number = models.CharField(max_length=10,null=True,default=" ")
    map_link = models.CharField(max_length=200,null=True,default=" ")
    mess = models.CharField(max_length=50,null=True,default=" ")
    hostel_img_1=models.ImageField(upload_to='images/',default=" " ,null=True,blank=True)
    hostel_img_2=models.ImageField(upload_to='images/',default=" " ,null=True,blank=True)
    hostel_img_3=models.ImageField(upload_to='images/',default=" " ,null=True,blank=True)
    def __str__(self):
           return f'{self.hostel_name}'         

# RUN server