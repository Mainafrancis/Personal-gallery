from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Image,Location,Category

#Create your views here.
def image(request):
    image = Image.get_all()