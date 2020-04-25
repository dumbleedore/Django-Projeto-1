from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    value = models.DecimalField('Value', decimal_places=2, max_digits=4)
    qty = models.IntegerField('Quantity')

    def __str__(self):
        return self.name


class Client(models.Model):
    name_client = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return f'{self.name_client} {self.last_name}'
