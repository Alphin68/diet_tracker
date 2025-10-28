from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    BLOOD_CHOICE=[
        ('A+','A+'),
        ('B+','B+'),
        ('A-','A-'),
        ('B-','B-'),
        ('AB+','AB+'),
        ('AB-','AB-'),
        ('O+','O+'),
        ('O-','O-')
        ]
    GENDER_CHOICE=[
        ('MALE','MALE'),
        ('FEMALE','FEMALE'),
        ('OTHER','OTHER')
        ]
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    weight = models.FloatField(null=True)
    height = models.FloatField(null=True)
    gender = models.CharField(choices=GENDER_CHOICE,null=True,blank=True, max_length=10)
    blood_group= models.CharField(choices=BLOOD_CHOICE, max_length=5)
    phone_number = models.CharField(null=True, max_length=15)
    

    def __str__(self):
        return f'{self.user.username} Profile'
    