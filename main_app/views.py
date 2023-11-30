from django.shortcuts import render, redirect 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Guide, Order
from .forms import OrderForm, CommentForm
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse



# Create your views here.
def home(request):
    return render(request, 'home.html')

# Path for About Page
def about(request):
    return render(request, 'about.html')

# Path for Shop All Gudies Page
def guides_index(request):
    guides = Guide.objects.all()
    return render(request, 'guides/index.html', {'guides': guides})

# detail page
def guides_detail(request, guide_id):
    guide = Guide.objects.get(id = guide_id)
    order_form = OrderForm()
    comment_form = CommentForm()
    return render(request, 'guides/detail.html', {
        'guide': guide,
        'order_form': order_form,
        'comment_form': comment_form})

# Step 4: Create full CRUD for Order
class OrderList(ListView):
    model = Order

class OrderDetail(DetailView):
    model = Order

class OrderCreate(CreateView):
    model = Order
    fields = '__all__'
    success_url = '/orders/'

class OrderUpdate(UpdateView):
    model = Order
    fields = ['date']

class OrderDelete(DeleteView):
    model = Order
    success_url = '/orders/'


def create_order(request, guide_id):
    form = OrderForm(request.POST)
    if form.is_valid():
        order = form.save(commit=False)
        order.guide_id = guide_id
        order.save()
    # Redirect to a success page or do something else
        return redirect(reverse('orders_index'))
    return render(request, 'gudies/detail.html', {'guide_id': guide_id})


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def add_comment(request, guide_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.guide_id = guide_id
        new_comment.save()
    return redirect('detail', guide_id=guide_id)

   
