from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Image, Location, Category

# Create your views here.
def home(request):
  images = Image.get_all_images()
  return render(request, 'index.html',{"images":images})

# Display the details of a photo
def image_details(request, photo_id):
  try:
    pic_details = Image.objects.get(pk = photo_id)
  except DoesNotExist:
    raise Http404()
  return render(request, "detailedPic.html", {"details":pic_details})