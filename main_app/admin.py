from django.contrib import admin
from .models import Guide, Order, User

# Register your models here.
admin.site.register(Guide)
admin.site.register(Order)
admin.site.register(User)
