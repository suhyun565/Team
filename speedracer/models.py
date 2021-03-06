from django.db import models

# Create your models here.

class Manager(models.Model):

	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


class Product(models.Model):
	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name




class Order(models.Model):
	STATUS = (
			('Entering', 'Entering'),
			('Releasing', 'Releasing'),
			)
	manager = models.ForeignKey(Manager, null=True, on_delete= models.SET_NULL)
	product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	count = models.IntegerField(default=0)

	def __str__(self):
		return self.product.name

class Inventory(models.Model):
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL,blank=True)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL,blank=True)
    current_amount = models.IntegerField(default=0)
    product_location = models.CharField(max_length=10, blank= False)

    class Meta:
        db_table = 'inventory'

    def __str__(self):
        return self.product.name





