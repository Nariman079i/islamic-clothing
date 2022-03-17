from django.shortcuts import render

def index(request):

    titles = {
        'ico':'hello world',
        'title_doc':'test dictionary'
    }
    url_file = 'main/index.html'
    context = {
        'title':titles
    }
    return render(request , url_file , context=context)
