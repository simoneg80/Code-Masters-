from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Guide, Order
from .forms import OrderForm
from django.views.generic import ListView, DetailView


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
    return render(request, 'guides/detail.html', {
        'guide': guide,
        'order_form': order_form})

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
    # if request.method == 'POST':
    form = OrderForm(request.POST)
    if form.is_valid():
            # # Get the user object for the current logged-in user
            # user = request.user

            # Save the form with the user information
        order = form.save(commit=False)
        order.guide_id = guide_id
        order.save()

            # Redirect to a success page or do something else
    return redirect('detail', guide_id=guide_id)
    # else:
    #     form = OrderForm()

        # return render(request, 'order_form.html', {'form': form})