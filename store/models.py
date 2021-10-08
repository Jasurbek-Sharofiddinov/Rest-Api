from django.db import models

# Create your models here.

class Product(models.Model):
	title=models.CharField(max_length=255,null=True,blank=False)
	description=models.TextField()
	price=models.DecimalField(max_digits=6,decimal_places=2)
	inventory=models.IntegerField()
	last_update=models.DateTimeField(auto_now=True)

class Customer(models.Model):
	first_name=models.CharField(max_length=255,null=True,blank=False)
	last_name=models.CharField(max_length=255,null=True,blank=False)
	email=models.CharField(max_length=50,null=False,blank=False,unique=True)
	phone=models.CharField(max_length=50,null=True,blank=True)
	birth_date=models.DateTimeField(null=True)