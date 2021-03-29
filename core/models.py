from django.db import models
from django.contrib.auth.models import User


# Products in Store
class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    weight = models.FloatField(null=True)
    color = models.CharField(max_length=100, null=True)
    euler_char = models.IntegerField(null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


# Customers of the Store
class Customer(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


# Baskets for Customers
class Basket(models.Model):
    customer = models.OneToOneField(
        Customer, null=True, blank=True, on_delete=models.SET_NULL)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']

    def __str__(self):
        return str(self.customer) + "_basket"