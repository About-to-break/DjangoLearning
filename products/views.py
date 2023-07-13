from django.shortcuts import render

# Create your views here.

#Функции = контроллеры

def index(request):
    context = {
        'title': 'Store',
        'is_promotions': False,
        }
    return render(request, 'products/index.html', context)

def products(request):
    return render(request, 'products/products.html')

