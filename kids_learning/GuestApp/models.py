from django.db import models




class login(models.Model):
    LoginId = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=20)

from AdminApp.models import tbl_location

class tbl_parent(models.Model):
    parentid = models.AutoField(primary_key=True)
    parentname = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phno = models.BigIntegerField()
    address = models.CharField(max_length=100,null=True)
    loginid = models.ForeignKey(login, on_delete=models.CASCADE)
    locationid = models.ForeignKey(tbl_location, on_delete=models.CASCADE)
