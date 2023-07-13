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
    context = {
        'title': 'Store - каталог',
        'products': [
            {'image': "/static/vendor/img/products/Adidas-hoodie.png",
             'name': "Худи черного цвета с монограммами adidas Originals",
             'price': 6090,
             'description': "Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни."
             },
            {'image': "/static/vendor/img/products/Black-Dr-Martens-shoes.png",
             'name': "Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex",
             'price': 13590,
             'description': "Гладкий кожаный верх. Натуральный материал."
             }
        ]
    }
    return render(request, 'products/products.html', context)

