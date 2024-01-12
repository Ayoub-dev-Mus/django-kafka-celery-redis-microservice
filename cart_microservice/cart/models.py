from django.db import models
from django.contrib.postgres.fields import ArrayField


class Cart(models.Model):
    user_id = models.IntegerField()
    product_ids = ArrayField(models.IntegerField(), default=list)
    quantity = models.IntegerField( default=1)
