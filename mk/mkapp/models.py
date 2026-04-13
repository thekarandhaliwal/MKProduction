from django.db import models

# Create your models here.
# models.py
from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=100, unique=True)
    amount = models.FloatField()
    status = models.CharField(max_length=20, default="PENDING")  # PENDING / PAID / FAILED
    cf_payment_id = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_id