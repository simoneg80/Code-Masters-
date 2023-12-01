from django.forms import ModelForm
from .models import Guide, Order, Comment

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['user']



class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['review']
        



