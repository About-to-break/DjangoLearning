from django.shortcuts import render

# Create your views here.

#Функции = контроллеры

def index(request):
    return render(request, 'products/index.html')