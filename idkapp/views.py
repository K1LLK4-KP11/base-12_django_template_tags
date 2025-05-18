from django.shortcuts import render

# Create your views here.
def huh(request):
    fruits = ["Яблоко", "Банан", "Вишня"]
    return render(request, 'smth.html') 