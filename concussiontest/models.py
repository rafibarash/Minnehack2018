from django.db import models

class Athlete(models.Model):
    first = models.CharField(max_length=15, default='')
    last = models.CharField(max_length=15, default='')
    base_time = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    base_errors = models.IntegerField(default=0)

    def __str__(self):
        return self.first + " " + self.last


