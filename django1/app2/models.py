from django.db import models
import datetime
# Create your models here.
class sale(models.Model):
    itemname = models.CharField(max_length=30)
    day = models.DateTimeField()
    time1 =  models.DateTimeField()