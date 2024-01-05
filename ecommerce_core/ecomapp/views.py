from django.shortcuts import render, redirect
from .models import Product,Category
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms
# Create your views here.
def home(request):
    product_objects = Product.objects.all()
    
   #search
    product_name = request.GET.get('product_name')

    if product_name != '' and product_name is not None:
        product_objects = product_objects.filter(title__icontains = product_name)
    #paginator
    paginator = Paginator(product_objects, 10)  # Show 10 contacts per page.
    page = request.GET.get("page")
    product_objects = paginator.get_page(page)
        
    return render(request, 'ecomapp/index.html', {'product_objects': product_objects} )


class ProductDetailView(DetailView):
    model = Product
    template_name = 'ecomapp/product_detail.html'
    context_object_name = 'detail'


def category(request, foo):
    foo = foo.replace('-' , ' ')
    
    try:
        category = Category.objects.get(name = foo)
        product_objects = Product.objects.filter(category = category)
        paginator = Paginator(product_objects, 10)  # Show 10 contacts per page.
        page = request.GET.get("page")
        product_objects = paginator.get_page(page)
        return render (request, 'ecomapp/category.html', {'product_objects': product_objects, 'category': category})
    except:
        return redirect('ecom:index')




def contact(request):
    return render(request, 'ecom/contact.html' )

def about(request):
    return render(request, 'ecom/about.html' )


def login_page(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        userExist = User.objects.filter(username = username)

        if not userExist.exists():
            messages.error(request, ("User doesn't exist"))
            return redirect('ecom:login')
        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request, 'Invalid Credentials')
            return redirect('ecom:login')
        else:
            login(request, user)
            return redirect('ecom:index')


    return render(request, 'ecomapp/login.html')

def logout_page(request):
    logout(request)
    return redirect('ecom:login')

def register_user(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, ('You have registered successfully'))
            return redirect('ecom:index')
        else:
            messages.success(request, ('There was a problem please try again'))
            return redirect('ecom:register')

    else:
        return render(request, 'ecomapp/register.html', {'form': form})
