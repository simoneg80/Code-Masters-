from django.db import models

# Create your models here.
class Guide(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=100)
  price = models.IntegerField()

  def __str__(self):
    return f'{self.name} ({self.id})'