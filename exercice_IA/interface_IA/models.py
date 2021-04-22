from django.db import models

# Create your models here.


class Images(models.Model):
    title = models.CharField(max_length=50)
    result = models.FloatField()
    date = models.DateTimeField()
    weight = models.IntegerField()


    def __str__(self):
        return self.title