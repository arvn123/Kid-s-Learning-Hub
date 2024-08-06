from django.db import models

from AdminApp.models import tbl_daycare
from GuestApp.models import tbl_parent


# Create your models here.

class tbl_application(models.Model):
    application_id = models.AutoField(primary_key=True)
    parent_id = models.ForeignKey(tbl_parent, on_delete=models.CASCADE)
    daycare_id = models.ForeignKey(tbl_daycare, on_delete=models.CASCADE)
    child_name = models.CharField(max_length=100)
    child_age = models.IntegerField()
    child_gender = models.CharField(max_length=100)
    child_image= models.ImageField()
    child_healthdetails=models.CharField(max_length=500)
    application_status=models.CharField(max_length=20)
    application_no = models.BigIntegerField()