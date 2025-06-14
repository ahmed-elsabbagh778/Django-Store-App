from django.shortcuts import redirect, render
from django.views import View

from .forms import ProductForm, RegisterForm
from products.models import Categories, Product, User

# Create your views here.

def base(request):
    return render(request, 'base.html')

# def home(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         description = request.POST.get('description')
#         creation_date = request.POST.get('creation_date')
#         expiry_date = request.POST.get('expiry_date')
#         category = request.POST.get('category')
#         price = request.POST.get('price')
#         country = request.POST.get('country')
#         image = request.FILES.get('image') 

#         Product.objects.create(
#             name=name,
#             description=description,
#             creation_date=creation_date,
#             expiry_date=expiry_date,
#             category=Categories.objects.get(name=category),
#             price=price,
#             country=country,
#             image=image
#         )
#         return redirect('items')
    
#     username = request.session.get('username')
#     if not username:
#         return redirect('login')

#     return render(request, 'products/home.html', {'categories': Categories.objects.all()})


def home(request):
    if not request.session.get('username'):
        return redirect('login')

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('items')
    else:
        form = ProductForm()

    return render(request, 'products/home.html', {'form': form})

# def items(request):
#     products = Product.objects.all()
#     categories = Categories.objects.all()
#     username = request.session.get('username')
#     if not username:
#         return redirect('login')
#     return render(request, 'products/items.html', {'products': products , 'categories': categories})

class Items(View):

    def get(self, request):
        username = request.session.get('username')
        if not username:
            return redirect('login')

        products = Product.objects.all()
        categories = Categories.objects.all()

        return render(request, 'products/items.html', {
            'products': products,
            'categories': categories
        })

def delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('items')

def update(request, id):
    product = Product.objects.get(id=id)
    
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        product.creation_date = request.POST.get('creation_date')
        product.expiry_date = request.POST.get('expiry_date')
        product.category = Categories.objects.get(name=request.POST.get('category'))
        product.price = request.POST.get('price')
        product.country = request.POST.get('country')

        if request.FILES.get('image'):
            product.image = request.FILES['image']

        product.save()
        return redirect('items')
    

# def register(request):
#     if request.method == 'POST':
#         if request.POST.get('password') == request.POST.get('confirm_password'):
#             User.objects.create(
#                     username=request.POST.get('username'),
#                     email=request.POST.get('email'),
#                     password=request.POST.get('password')
#                 )
#             return redirect('login')
            
#     return render(request, 'register.html')

def register(request):
    if request.method == 'POST':
        registerForm = RegisterForm(request.POST)
        if registerForm.is_valid():
            User.objects.create(
                username=request.POST.get('username'),
                email=request.POST.get('email'),
                password=request.POST.get('password')
            )
            return redirect('login')
    else:
        registerForm = RegisterForm()
        
    return render(request, 'register.html', {'registerForm': registerForm})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = User.objects.get(username=username)

        if user.password == password:
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            return redirect('home')
        return render(request, 'login.html')

    return render(request, 'login.html')

def logout(request):
    request.session.flush()
    return redirect('login')