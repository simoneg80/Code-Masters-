from django.forms import ModelForm
from .models import Guide, Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
        
