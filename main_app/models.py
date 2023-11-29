from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Guide(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=100)
  price = models.IntegerField()

  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.name} ({self.id})'