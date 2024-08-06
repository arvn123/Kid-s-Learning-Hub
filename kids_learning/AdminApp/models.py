from django.db import models



# Create your models here.
class tbl_district(models.Model):
    districtid = models.AutoField(primary_key=True)
    districtname = models.CharField(max_length=50)


class tbl_category(models.Model):
    categoryid = models.AutoField(primary_key=True)
    categoryname = models.CharField(max_length=50)
    categoryimage = models.ImageField()


class tbl_location(models.Model):
    locationid = models.AutoField(primary_key=True)
    locationname = models.CharField(max_length=50)
    districtid = models.ForeignKey(tbl_district, on_delete=models.CASCADE)

class tbl_subcategory(models.Model):
    subcategoryid=models.AutoField(primary_key=True)
    subcategoryname=models.CharField(max_length=50)
    categoryid=models.ForeignKey(tbl_category, on_delete=models.CASCADE)
    subcategoryimage = models.ImageField()

from GuestApp.models import login

class tbl_daycare(models.Model):
    daycare_id = models.AutoField(primary_key=True)
    location_id =models.ForeignKey(tbl_location, on_delete=models.CASCADE)
    daycare_landmark= models.CharField(max_length=50)
    daycare_pincode=models.IntegerField()
    branch_name=  models.CharField(max_length=50)
    daycare_image= models.ImageField()
    daycare_contact =models.BigIntegerField()
    description=models.CharField(max_length=50,null=True)
    daycare_email= models.CharField(max_length=50)
    login_id=models.ForeignKey(login, on_delete=models.CASCADE)
    daycare_map= models.CharField(max_length=50)
    application_fee=models.FloatField(null=True)
    monthly_fee=models.FloatField(null=True)

