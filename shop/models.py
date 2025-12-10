from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField()
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    password = models.CharField(30)

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    descriptions = models.TextField(blank=True, null=True)
    price = models.DecimalField(default=0, decimal_places=0, max_digits=12)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    picture = models.ImageField(upload_to='upload/product')
    star = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=0, max_digits=12)

    is_available = models.BooleanField(default=True)   

    def __str__(self):
        return self.name
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, blank=True)
    address = models.CharField(default='', blank=True)
    phone = models.CharField(max_length=20, blank=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.product