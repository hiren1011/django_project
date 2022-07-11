from django.db import models
from django.contrib.auth.hashers import check_password,make_password


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=10,default="")
    price = models.DecimalField(max_digits=12,decimal_places=2,default=0)
    des = models.TextField(max_length=300,default="")
    image = models.ImageField(upload_to='images/products')
    review = models.TextField(max_length=350)

    def __str__(self):
        return self.name
    

class Signup(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=254)
    phone = models.IntegerField(default=0)
    pswd = models.CharField(max_length=50)
    vendor = models.BooleanField(verbose_name=("Is a vendor"),default=False)


    def __str__(self):
        return self.name

