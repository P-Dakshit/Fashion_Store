from django.db import models
from django.contrib.auth.models import User

class cloth(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email =  models.CharField(max_length = 10)
    username = models.CharField(max_length=20)

class product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    product_name = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    image_link = models.URLField()

    def __str__(self):
        return self.product_name