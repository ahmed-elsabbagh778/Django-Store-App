from django.db import models

# Create your models here.


class Categories(models.Model):
    name= models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class Product(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    creation_date = models.DateField()
    expiry_date = models.DateField()
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True)
    price = models.FloatField()
    country = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
    

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    
    def __str__(self):
        return self.username
    

