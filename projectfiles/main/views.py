from django.shortcuts import render
from .models import *
def index(request):

    posts = Clothing.objects.all()

    url_file = 'main/index.html'



    return render(request , url_file  , context={'posts' : posts})
