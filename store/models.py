from django.db import models

# Create your models here.


class Promotion(models.Model):
	description=models.TextField()
	discount=models.FloatField()
#	product_set=models.

class Collection(models.Model):
	title=models.CharField(max_length=255)
	featured_product=models.ForeignKey(
		'Product',on_delete=models.SET_NULL,null=True,related_name='+')

class Product(models.Model):
	collection=models.ForeignKey(Collection,on_delete=models.PROTECT)
	title=models.CharField(max_length=255,null=True,blank=False)
	slug=models.SlugField(default='-')
	description=models.TextField()
	unit_price=models.DecimalField(max_digits=6,decimal_places=2)
	inventory=models.IntegerField()
	last_update=models.DateTimeField(auto_now=True)
	promotions=models.ManyToManyField(Promotion)

class Customer(models.Model):

	membership_choices=[
		('G','Gold'),
		('S','Silver'),
		('B','Bronze'),
	]

	first_name=models.CharField(max_length=255,null=True,blank=False)
	last_name=models.CharField(max_length=255,null=True,blank=False)
	email=models.CharField(max_length=50,null=False,blank=False,unique=True)
	phone=models.CharField(max_length=50,null=True,blank=True)
	birth_date=models.DateTimeField(null=True)
	membership=models.CharField(max_length=1,choices=membership_choices,default='B ')



class Order(models.Model):
	customer=models.ForeignKey(Customer,on_delete=models.PROTECT)
	payment_status_choices=[
		('P','Pending'),
		('C','Complete'),
		('F','Failed')
	]
	placed_at=models.DateTimeField(auto_now=True)
	payment_status=models.CharField(max_length=1,choices=payment_status_choices,default='P')

class OrderItem(models.Model):
	order=models.ForeignKey(Order,on_delete=models.CASCADE)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	quantity=models.PositiveSmallIntegerField()
	unit_price=models.DecimalField(max_digits=6,decimal_places=2)


class Address(models.Model):
	customer=models.OneToOneField(Customer,primary_key=True,on_delete=models.CASCADE)
	street=models.CharField(max_length=255)
	city=models.CharField(max_length=255)

class Cart(models.Model):
	created_at=models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
	cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	quantity=models.PositiveSmallIntegerField()


