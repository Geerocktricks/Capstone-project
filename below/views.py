from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    '''
    view function that displays the home page
    '''
    return render(request , 'index.html')