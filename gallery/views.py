from django.shortcuts import render
from django.http import HttpResponse
from .models import Image, Location, Category

# Create your views here.
def home(request):
  images = Image.get_all_images()
  return render(request, 'index.html',{"images":images})