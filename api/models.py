from django.db import models

# Definition of products model


class products(models.Model):
    name = models.TextField("Name", max_length=255)
    brand = models.TextField("Brand", max_length=50)
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    updated_at = models.DateTimeField("Updated at", auto_now=True)
