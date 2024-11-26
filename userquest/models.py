from django.db import models

from django.db import models
class PhotoSubmission(models.Model):
    photo = models.ImageField(upload_to='photos/')
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
# Create your models here.
