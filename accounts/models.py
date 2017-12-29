from django.db import models

# Create your models here.


class Notice(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    status = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)