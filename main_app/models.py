from django.db import models
from django.urls import reverse


# Step1: Create a model M:M Model for order
class Order(models.Model):
  date = models.DateField()
  

  def __str__(self):
    return f'Order # {self.id} on {self.date}'

  def get_absolute_url(self):
    return reverse('detail', kwargs={'pk': self.id})


# Create your models here.
class Guide(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=100)
  price = models.IntegerField()
# Step2: Add a ManyToManyField to Order
  orders = models.ManyToManyField(Order, blank=True)

  def __str__(self):
    return f'{self.name} ({self.id})'