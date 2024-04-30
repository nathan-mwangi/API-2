from django.db import models
class Brand(models.Model):
    Brand_name = models.CharField(max_length=100)
    Brand_size = models.IntegerField(null=False, blank=False)


# Create your models here.
