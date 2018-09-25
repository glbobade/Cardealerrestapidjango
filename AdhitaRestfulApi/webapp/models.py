from django.db import models


class car(models.Model):

    name = models.CharField(max_length=50)
    model_name = models.CharField(max_length=50)
    color = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class computer(models.Model):
    computer_name = models.CharField(max_length=50)
    computer_model_name = models.CharField(max_length=50)
    computer_color = models.CharField(max_length=20)

    def __str__(self):
        return self.computer_name