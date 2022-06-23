from datetime import datetime

from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=150)
    publisher = models.CharField(max_length=150)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title
