from django.contrib import admin
from .models import Categories, Product, User

admin.site.register(Product)
admin.site.register(Categories)
admin.site.register(User)
# Register your models here.
