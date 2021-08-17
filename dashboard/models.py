import self as self
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY = (
    ('Stationary', 'Stationary'),
    ('Electronics', 'Electronics'),
    ('Food', 'Food'),
)


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.name}'


class Supplier(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)
    company = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.category} supplied by {self.name} from {self.company}'


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    customer = models.CharField(max_length=100, null=True)
    amount = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.product.name} ordered by {self.customer} made by {self.staff}'
