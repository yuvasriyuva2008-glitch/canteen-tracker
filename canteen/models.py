from django.db import models

class FoodOrder(models.Model):
    customer_name = models.CharField(max_length=100)
    food_item = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()
    is_delivered = models.BooleanField()