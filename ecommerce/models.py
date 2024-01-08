from django.db import models

class User(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=20)

class Product(models.Model):
    pass