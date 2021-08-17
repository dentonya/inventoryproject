from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Order, Supplier
from .forms import ProductForm, OrderForm, SupplierForm
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.
@login_required(login_url='user-login')
def index(request):
    orders = Order.objects.all()
    products = Product.objects.all()
    clients = Supplier.objects.all()
    orders_count = orders.count()
    product_count = products.count()
    clients_count = clients.count()
    workers_count = User.objects.all().count()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()
    context = {
        'orders': orders,
        'form': form,
        'products': products,
        'product_count': product_count,
        'workers_count': workers_count,
        'orders_count': orders_count,
        'clients_count': clients_count,
    }
    return render(request, 'dashboard/index.html', context)


@login_required(login_url='user-login')
def staff(request):
    workers = User.objects.all()
    workers_count = workers.count()
    orders_count = Order.objects.all().count()
    clients_count = Supplier.objects.all().count()
    product_count = Product.objects.all().count()
    context = {
        'workers': workers,
        'workers_count': workers_count,
        'orders_count': orders_count,
        'clients_count': clients_count,
        'product_count': product_count
    }
    return render(request, 'dashboard/staff.html', context)


@login_required(login_url='user-login')
def staff_delete(request, pk):
    workers = User.objects.get(id=pk)
    if request.method == 'POST':
        workers.delete()
        return redirect('dashboard-staff')
    context = {
        'workers': workers
    }
    return render(request, 'dashboard/staff_delete.html', context)


def staff_detail(request, pk):
    workers = User.objects.get(id=pk)
    context = {
        'workers': workers,
    }
    return render(request, 'dashboard/staff_detail.html', context)


@login_required(login_url='user-login')
def product(request):
    items = Product.objects.all()
    product_count = items.count()
    workers_count = User.objects.all().count()
    orders_count = Order.objects.all().count()
    clients_count = Supplier.objects.all().count()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            return redirect('dashboard-product')
    else:
        form = ProductForm()
    context = {
        'items': items,
        'form': form,
        'workers_count': workers_count,
        'orders_count': orders_count,
        'clients_count': clients_count,
        'product_count': product_count,
    }
    return render(request, 'dashboard/product.html', context)


@login_required(login_url='user-login')
def product_detail(request, pk):
    items = Product.objects.get(id=pk)
    context = {
        'items': items,
    }
    return render(request, 'dashboard/staff_detail.html', context)


@login_required(login_url='user-login')
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')
    context = {
        'item': item
    }
    return render(request, 'dashboard/product_delete.html', context)


@login_required(login_url='user-login')
def product_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/product_update.html', context)


@login_required(login_url='user-login')
def supplier(request):
    clients = Supplier.objects.all()
    clients_count = clients.count()
    workers_count = User.objects.all().count()
    orders_count = Order.objects.all().count()
    product_count = Product.objects.all().count()
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-supplier')
    else:
        form = SupplierForm()
    context = {
        'clients': clients,
        'form': form,
        'workers_count': workers_count,
        'orders_count': orders_count,
        'clients_count': clients_count,
        'product_count': product_count,

    }
    return render(request, 'dashboard/supplier.html', context)


@login_required(login_url='user-login')
def supplier_delete(request, pk):
    clients = Supplier.objects.get(id=pk)
    if request.method == 'POST':
        clients.delete()
        return redirect('dashboard-supplier')
    context = {
        'clients': clients
    }
    return render(request, 'dashboard/supplier_delete.html', context)


@login_required(login_url='user-login')
def supplier_detail(request, pk):
    clients = Supplier.objects.get(id=pk)
    context = {
        'clients': clients,
    }
    return render(request, 'dashboard/supplier_detail.html', context)


@login_required(login_url='user-login')
def order(request):
    orders = Order.objects.all()
    orders_count = orders.count()
    workers_count = User.objects.all().count()
    clients_count = Supplier.objects.all().count()
    product_count = Product.objects.all().count()
    context = {
        'orders': orders,
        'workers_count': workers_count,
        'orders_count': orders_count,
        'clients_count': clients_count,
        'product_count': product_count,
    }
    return render(request, 'dashboard/order.html', context)


@login_required(login_url='user-login')
def order_detail(request, pk):
    orders = Order.objects.get(id=pk)
    context = {
        'orders': orders,
    }
    return render(request, 'dashboard/order_detail.html', context)
    print(orders)
    return render(request, 'dashboard/order_detail.html', context)


@login_required(login_url='user-login')
def order_delete(request, pk):
    orders = Order.objects.get(id=pk)
    if request.method == 'POST':
        orders.delete()
        return redirect('dashboard-order')
    context = {
        'orders': orders
    }
    return render(request, 'dashboard/order_delete.html', context)
