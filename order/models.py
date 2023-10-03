from django.db import models
from uuid import uuid4
from cart.models import Cart
from shop.models import Product
from authentication.models import User

# Create your models here.

class Order(models.Model):
    PENDING='P'
    SHIPPED='S'
    DELIVERED='D'
    STATUS_CHOICE = [
        (PENDING, 'PENDING'),
        (SHIPPED, 'SHIPPED'),
        (DELIVERED, 'DELIVERED'),
    ]
    PAYED='P'
    NOTPAYED='N'
    ONDELIVERY='S'
    PAYMENT_STATUS_CHOICE = [
        (PAYED, 'PAYED'),
        (NOTPAYED, 'NOTPAYED'),
        (ONDELIVERY, 'ONDELIVERY'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    cart = models.ForeignKey(Cart, on_delete=models.PROTECT, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, default=PENDING)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICE, default=NOTPAYED)
    address = models.CharField(max_length=550)

    def __str__(self):
        return str(self.id)
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='items')
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return str(self.order.id)
