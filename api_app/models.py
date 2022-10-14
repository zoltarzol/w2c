from django.db import models

# Create your models here.
class ApiModel(models.Model):
    slug = models.CharField(
        max_length=100,
        blank=False,
        null=True
        )

    convert = models.CharField(
        max_length=100,
        blank=False,
        null=True
        )