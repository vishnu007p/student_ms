from django.db import models

# Create your models here.
class studentdetail(models.Model):
    sname=models.CharField(max_length=200)
    semail=models.EmailField(max_length=200)
    snumber=models.IntegerField()
    sage=models.IntegerField()
    senrollment_date=models.DateField(max_length=50)
    scourse=models.CharField(max_length=50)
    