from django.shortcuts import render
from core.models import Car

def home(request):
    cars = Car.objects.all()
    context = {
        'cars':cars
    }
    return render(request, 'index.html', context)
