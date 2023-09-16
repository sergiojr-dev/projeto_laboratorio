from django.db import models

# Create your models here.
class Laboratory(models.Model):
    name_laboratory = models.CharField(max_length=20)
    number_laboratory = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)


class Schedule_Lab(models.Model):
    lab = models.ForeignKey(Laboratory, on_delete=models.CASCADE)
    rent_date = models.DateField()
    available_hour = models.TimeField()
    rent_hour = models.TimeField()