from django.shortcuts import redirect, render

from products.models import Product

# Create your views here.

def base(request):
    return render(request, 'base.html')

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        creation_date = request.POST.get('creation_date')
        expiry_date = request.POST.get('expiry_date')
        category = request.POST.get('category')
        price = request.POST.get('price')
        country = request.POST.get('country')
        image = request.FILES.get('image') 

        Product.objects.create(
            name=name,
            description=description,
            creation_date=creation_date,
            expiry_date=expiry_date,
            category=category,
            price=price,
            country=country,
            image=image
        )
        return redirect('items')

    return render(request, 'products/home.html', {'categories': Product.categories })

def items(request):
    products = Product.objects.all()
    return render(request, 'products/items.html', {'products': products})