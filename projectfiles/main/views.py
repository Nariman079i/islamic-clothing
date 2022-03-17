from django.shortcuts import render
from .models import *
def index(request):


    url_file = 'main/index.html'
    posts = Clothing.objects.all()

    context = {
        'posts':posts
    }
    return render(request , url_file  ,context)
