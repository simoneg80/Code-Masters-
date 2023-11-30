from django.contrib import admin
from .models import Guide, Order, Comment

# Register your models here.
admin.site.register(Guide)
admin.site.register(Order)
admin.site.register(Comment)

