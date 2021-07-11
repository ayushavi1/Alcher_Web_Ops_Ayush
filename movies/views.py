from django.shortcuts import render

def home(request):
    return render(request, 'movies/home.html')


def login(request):
    return render(request, 'movies/login.html', {'title':'Login'})