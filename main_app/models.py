from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


#comment model
class Comment(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  date= models.DateField()
  review = models.CharField(max_length=5000)

  guide = models.ForeignKey(Guide, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.user} - {self.date} - {self.review}"




# Step1: Create a model M:M Model for order
class Order(models.Model):
  date = models.DateField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)

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