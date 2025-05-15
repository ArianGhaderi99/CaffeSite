from django.db import models

# Create your models here.

class Order(models.Model):
    Addres=models.CharField(max_length=254)
    phone_number=models.TextField(max_length=12)
    coffee_type=models.TextField(max_length=40)
    weight=models.TextField(max_length=4)
    
    def __str__(self):
        return self.phone_number
    
    
class Contact(models.Model):
    number=models.TextField(max_length=12)
    email=models.EmailField(primary_key=True)
    
    def __str__(self):
        return self.email