from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Command(models.Model):
    command = models.CharField(max_length=200)
    delay = models.IntegerField(validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])
    status = models.Choices("Success", "Failure")


class BasicConfiguration(models.Model):
    stationId = models.IntegerField()
    serverUrl = models.CharField(max_length=128)
