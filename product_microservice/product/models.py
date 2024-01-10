from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    weight = models.IntegerField()
    reference = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='product_images', blank=True)

    def __str__(self):
        return self.name