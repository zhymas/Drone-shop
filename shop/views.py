from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return render(request, 'shop/index.html')