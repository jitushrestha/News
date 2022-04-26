from django.db import models

# Create your models here.
class AdminLogin(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    
    class Meta:
        db_table = "admin_login"


#reporter register/login
class RpLogin(models.Model):
    firstname = models.CharField(max_length=50, null=True)
    lastname = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=50, null=True)
    image_url = models.FileField(upload_to='images/users', null=True)
    id_approve = models.BooleanField(null=True)
    verified = models.BooleanField(null=True, default=False)
    
    class Meta:
        db_table = "rp_login"



# add_report 
class AddReport(models.Model):
    image = models.FileField(upload_to='images')
    Date = models.DateField(max_length=100)
    Title = models.CharField(max_length=100)
    Description = models.CharField(max_length=10000)
    approval = models.BooleanField(null=True)
    Type = models.CharField(max_length=100, null=True)
    reporterid = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = "addreport"       
