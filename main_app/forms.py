from django.forms import ModelForm
from .models import Guide, Order, Comment

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = "__all__"



class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['review']
        
