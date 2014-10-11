from django.db import models

# Create your models here.
class dutyTable(models.Model):
    year_month = models.CharField(max_length=20)
    xlsfile = models.FileField(upload_to='./upload/duty/')

    def __unicode__(self):
        return self.year_month

class orderTable(models.Model):
    fileName = models.CharField(max_length=50)
    xlsfile = models.FileField(upload_to='./upload/order/')

    def __unicode__(self):
        return self.fileName