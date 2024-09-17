from django.shortcuts import render


def about(request):
    ''' Return about '''

    return render(request, 'about.html') 
