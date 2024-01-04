from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name



class Product(models.Model):

    def __str__(self):
        return self.title

    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE, default =1)
    typ = models.TextField()
    description = models.TextField()
    image = models.CharField(max_length = 5000)
