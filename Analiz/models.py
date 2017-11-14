from django.db import models

# Create your models here.mak
class task(models.Model):
    taskid = models.IntegerField()
    mainTask = models.CharField(max_length=1000)
    minrange = models.IntegerField()
    maxrange = models.IntegerField()
    def publish(self):
        self.save()

    def __str__(self):
        return self.mainTask