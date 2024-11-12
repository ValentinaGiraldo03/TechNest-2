from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.utils.translation import gettext as _
from .forms import UserRegisterForm, ClientRegisterForm
from product.forms import ProductForm
from product.models import Product
from .models import Administrator
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test


def is_admin(user):
    return user.is_authenticated and user.is_staff


def register_client(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        client_form = ClientRegisterForm(request.POST)
        if user_form.is_valid() and client_form.is_valid():
            user = user_form.save()
            client = client_form.save(commit=False)
            client.user = user
            client.save()
            login(request, user)
            messages.success(request, _('Registration successful. Welcome!'))
            return redirect('login')
    else:
        user_form = UserRegisterForm()
        client_form = ClientRegisterForm()
    
    return render(request, 'registerClient.html', {'user_form': user_form, 'client_form': client_form})


def register_administrator(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.is_staff = True  
            user.save()

            administrator = Administrator(user=user)
            administrator.save()

            login(request, user)
            messages.success(request, _('Administrator account created successfully. Welcome!'))
            return redirect('home')
    else:
        user_form = UserRegisterForm()
    
    return render(request, 'registerAdministrator.html', {'user_form': user_form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, _('Welcome {username}!').format(username=username))
                return redirect('home')
            else:
                messages.error(request, _('Invalid username or password.'))
        else:
            messages.error(request, _('Invalid username or password.'))
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


@user_passes_test(is_admin)
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, _('Product added successfully'))
            return redirect('home')
    else:
        form = ProductForm()
    
    return render(request, 'addProduct.html', {'form': form})


@user_passes_test(is_admin)
def edit_product(request, producto_id):
    producto = get_object_or_404(Product, id=producto_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, _('Product updated successfully'))
            return redirect('home')
    else:
        form = ProductForm(instance=producto)
    
    return render(request, 'editProduct.html', {'form': form, 'producto': producto})


@user_passes_test(is_admin)
def delete_product(request, producto_id):
    producto = get_object_or_404(Product, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, _('Product deleted successfully'))
        return redirect('home')
    
    return render(request, 'deleteProduct.html', {'producto': producto})
