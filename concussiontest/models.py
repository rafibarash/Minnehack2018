from django.db import models

class Athlete(models.Model):
    name = models.CharField(max_length=30, default='')
    slug = models.SlugField(max_length=50, default='', unique=True)
    base_time = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    new_time_1 = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    new_time_2 = models.DecimalField(max_digits=3, decimal_places=2, default=0)
