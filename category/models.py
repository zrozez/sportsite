from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128)
    information = models.TextField(null=True)