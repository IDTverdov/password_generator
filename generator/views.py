from django.shortcuts import render
import random

def home(request):
    return render(request, 'generator/home.html')


def password(request):
    thepassword = ''
    word = 'abcdefghijklmnopuvwxyz'
    characters = list(word)
    length = int(request.GET.get('length', 8))
    if request.GET.get('uppercase'):
        characters.extend(list(word.upper()))
    if request.GET.get('digit'):
        characters.extend(list('0123465789'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    for _ in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})

def about(request):
    return render(request, 'generator/about.html')