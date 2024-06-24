from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    profile_pic = models.ImageField(upload_to='media/profile_pic', blank=True, null=True)
    groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set', blank=True)

    def __str__(self):
        return self.username



class AddComputer(models.Model):
    compname = models.CharField(max_length=200)
    comploc = models.CharField(max_length=200)
    idadd = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.compname


class AddCyberUser(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    mobilenumber = models.CharField(max_length=15)  # Use CharField to handle phone number formatting
    email = models.EmailField(max_length=200)
    computeruse = models.ForeignKey(AddComputer, on_delete=models.DO_NOTHING)
    idproof = models.CharField(max_length=200)
    entryid = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    remark = models.CharField(max_length=200, blank=True, null=True)  # Assuming remark can be blank or null
    status = models.CharField(max_length=200, default='')  # Default can be an empty string
    fees = models.IntegerField(default=0)
    def __str__(self):
        return self.name
