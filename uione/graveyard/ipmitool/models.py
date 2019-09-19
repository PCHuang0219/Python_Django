from django.db import models

# Create your models here.
"""
class s3(models.Model):
    sensor = models.CharField(max_length=30)
    status = models.CharField(max_length=40)
    s2 = models.CharField(max_length=40)
    s3 = models.CharField(max_length=40)
    s4 = models.CharField(max_length=40)
    reading = models.IntegerField(blank=True)
    email = models.EmailField(blank=True, verbose_name='email')

Status | Sensor              | Reading  | Low Limit | High Limit |
------ | ---------           | -------  | --------- | ---------- |
OK     | (7) CPU1 Temp       |-----Low  | --------- | ---------- |
OK     | (8) CPU2 Temp       |-----Low  | --------- | ---------- |
OK     | (9) System Temp     |63C/145F  |   -5C/23F |   75C/167F |
OK     | (10) CPU1 Vcore     | 0.92 V   |    0.82 V |     1.35 V |
"""

class t1(models.Model):
    sensor = models.CharField(max_length=30)
    status = models.CharField(max_length=20)
    reading = models.CharField(max_length=20)
    low_limit = models.CharField(max_length=20)
    high_limit = models.CharField(max_length=20)
    s1 = models.CharField(blank=True, max_length=20)
    i1 = models.IntegerField(blank=True)
    f1 = models.FloatField(blank=True)
    stamp = models.DateTimeField(blank=True)

    def __str__(self):
        return u'%s %s ' % (self.sensor,self.status)

    class Meta:
        ordering = ['sensor']



