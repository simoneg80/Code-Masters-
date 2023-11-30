from django.forms import ModelForm
from .models import Guide, User

class OrderForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        
