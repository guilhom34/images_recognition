from django.db import models

# Create your models here.


class Images(models.Model):
    date = models.DateTimeField()
    name = models.CharField(max_length=50)
    size = models.IntegerField()
    result = models.CharField(max_length=200)

    def __init__(self, date, name, size, result):
        self.name = name
        self.result = result
        self.date = date
        self.size = size

    def __str__(self):
        return self.name
        return self.date
        return self.size
        return self.result
