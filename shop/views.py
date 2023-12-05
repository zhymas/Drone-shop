from django.shortcuts import render
from django.http import JsonResponse
from .models import Drone

def home(request):
    return render(request, 'shop/index.html')


def product(request):
    drones = Drone.objects.all()
    context = {
        'drones': drones
        }
    return render(request, 'shop/product.html', context)