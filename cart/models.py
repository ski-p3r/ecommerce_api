from django.db import models
from uuid import uuid4
from shop.models import Product

# Create your models here.

class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.cart.id)