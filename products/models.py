from django.db import models

# Create your models here.


class Product(models.Model):
    # categories = [
    #     ('Fruits', 'Fruits'),
    #     ('Vegetables', 'Vegetables'),
    #     ('Spices', 'Spices'),
    #     ('Dairy', 'Dairy'),
    # ]


    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    creation_date = models.DateField()
    expiry_date = models.DateField()
    category = models.CharField(max_length=20)
    price = models.FloatField()
    country = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
    

