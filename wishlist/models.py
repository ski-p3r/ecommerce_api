from django.db import models
from uuid import uuid4
from shop.models import Product

# Create your models here.

class Wishlist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.cart.id)