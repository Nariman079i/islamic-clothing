from django.shortcuts import render
from .models import *
def index(request):


    url_file = 'main/index.html'



    return render(request , url_file )
