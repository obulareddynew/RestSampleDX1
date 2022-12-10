from django.db import models

# Create your models here.
class Address(models.Model):
    homeNo=models.CharField(max_length=10)
    post=models.CharField(max_length=30)
    dist=models.CharField(max_length=30)
    state=models.CharField(max_length=10)
    pin=models.IntegerField()


class Person(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    sex=models.CharField(max_length=2)
    color=models.CharField(max_length=30)
    address=models.ForeignKey(Address,related_name='person',on_delete=models.CASCADE)

