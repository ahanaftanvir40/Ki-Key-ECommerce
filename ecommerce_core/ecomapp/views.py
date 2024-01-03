from django.shortcuts import render
from .models import Product
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator
# Create your views here.
def home(request):
    product_objects = Product.objects.all()
   #search
    product_name = request.GET.get('product_name')

    if product_name != '' and product_name is not None:
        product_objects = product_objects.filter(title__icontains = product_name)
    #paginator
    paginator = Paginator(product_objects, 3)  # Show 10 contacts per page.
    page = request.GET.get("page")
    product_objects = paginator.get_page(page)
        
    return render(request, 'ecomapp/index.html', {'product_objects': product_objects} )


class ProductDetailView(DetailView):
    model = Product
    template_name = 'ecomapp/product_detail.html'
    context_object_name = 'detail'

def contact(request):
    return render(request, 'ecom/contact.html' )

def about(request):
    return render(request, 'ecom/about.html' )