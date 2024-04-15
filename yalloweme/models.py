from django.utils import timezone
from django.db import models
from django.contrib.postgres.fields import ArrayField

class Transaction(models.Model):
    date = models.DateTimeField(auto_now_add=True, blank=True)
    amount = models.FloatField()
    payers = ArrayField(models.IntegerField())
    owers = ArrayField(models.IntegerField())
    description = models.CharField(max_length=500)

    def __str__(self):
        return '$' + self.amount

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    trips = ArrayField(models.IntegerField(), blank=True)

    def __str__(self):
        return 'User: ' + self.name + ' - ' + self.email

class Trip(models.Model):
    name = models.CharField(max_length=100)
    users = ArrayField(models.IntegerField(), blank=True)
    transactions = ArrayField(models.IntegerField(), blank=True)

    def __str__(self):
        return 'Trip: ' + self.name