from django.shortcuts import render
from .models import Product
from django.views.generic.detail import DetailView
# Create your views here.
def home(request):
    product_objects = Product.objects.all()
    context = {
        'product_objects': product_objects
    }
    return render(request, 'ecomapp/index.html', context )


class ProductDetailView(DetailView):
    model = Product
    template_name = 'ecomapp/product_detail.html'
    context_object_name = 'detail'

def contact(request):
    return render(request, 'ecom/contact.html' )

def about(request):
    return render(request, 'ecom/about.html' )