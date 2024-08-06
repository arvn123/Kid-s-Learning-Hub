from django.db import models

from AdminApp.models import tbl_subcategory, tbl_daycare
from ParentApp.models import tbl_application


# Create your models here.
class tbl_progress(models.Model):
    progressid=models.AutoField(primary_key=True)
    subcategoryid = models.ForeignKey(tbl_subcategory, on_delete=models.CASCADE)
    daycareid=models.ForeignKey(tbl_daycare, on_delete=models.CASCADE)
    applicationid=models.ForeignKey(tbl_application, on_delete=models.CASCADE)
    description=models.CharField(max_length=250)
    grade=models.CharField(max_length=10)
    pro_date=models.DateField(auto_now_add=True,null=True)

class tbl_payment(models.Model):
    paymentid=models.AutoField(primary_key=True)
    application=models.ForeignKey(tbl_application, on_delete=models.CASCADE)
    daycare=models.ForeignKey(tbl_daycare, on_delete=models.CASCADE)
    status=models.CharField(max_length=10)
    pdate=models.DateField(auto_now_add=True)