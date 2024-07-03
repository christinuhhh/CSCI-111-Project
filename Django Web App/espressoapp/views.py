#from django.contrib.auth import logout
#from django.shortcuts import render, redirect, get_object_or_404
from .models import Instance


# Create your views here.

def check(request):
    instances = Instance.objects.all()
    #return render(request, 'espressoapp/home.html', {'home':dish_objects})

