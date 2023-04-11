from django.shortcuts import render


def index(request):
    ''' Return homepage '''

    return render(request, 'home/index.html')
