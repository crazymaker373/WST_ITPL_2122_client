from django.db import models

# Create your models here.
class Command(models.Model):
    command = models.CharField(max_length=200)
    status = models.Choices("Success", "Failure")

    def __str__(self):
        return self.command