from datetime import timezone, datetime, timedelta

from djongo import models


# Create your models here.

class PredictionResult(models.Model):
    class_name = models.TextField()
    accuracy = models.FloatField()

    class Meta:
        abstract = True

    def __str__(self):
        return 'PredictionResult(class_name=\'{}\',accuracy=\'{}\')'.format(self.class_name, self.accuracy)


class Image(models.Model):
    _id = models.ObjectIdField()
    date = models.DateTimeField()
    name = models.TextField()
    size = models.IntegerField()
    result = models.ArrayField(
        model_container=PredictionResult
    )

    def get_id(self):
        return self._id

    def get_fomatted_results(self):
        res = {res_line['class_name']: '{:.2%}'.format(res_line['accuracy']) for res_line in sorted(self.result, key= lambda item: item['accuracy'], reverse=True)}
        return res

    def __str__(self):
        return 'Image(date=\'{}\',name=\'{}\',size=\'{}\',result=\'{}\')'.format(self.date, self.name,self.size,self.result)
