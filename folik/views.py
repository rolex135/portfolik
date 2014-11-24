from django.shortcuts import render

def home_page(request):
    return render (request, 'home.html')

def kontakt_page(request):
    return render(request, 'kontakt.html')

def works_page(request):
    return render(request, 'works.html')

def oskused_page(request):
    return render(request, 'oskused.html')
