from django.db import models
import datetime
# Create your models here.

# category of the product
class Category(models.Model):
    name = models.CharField(max_length=58)
    
    def __str__(self):
        return self.name
    
    #@daverobb2011
    class Meta:
        verbose_name_plural = 'categories'
    

class Customer(models.Model):
    first_name = models.CharField(max_length=58)
    last_name = models.CharField(max_length=58)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=58)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


#all off our product
class Product(models.Model):
    name = models.CharField(max_length=58)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')
    
    # Add sales
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    
    def __str__(self):
        return self.name
    
#customer orders
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=20, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.product