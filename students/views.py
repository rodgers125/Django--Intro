
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def About(request):
    return render(request, 'about.html')


def Contact(request):
    return render(request, 'contact.html')

def Classes(request):
    return render(request, 'classes.html')