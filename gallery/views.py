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

# Search pictures by category
def search_photos(request):
  
  locations = Location.objects.all()
  categories = Category.objects.all()
    
  if 'category' in request.GET and request.GET['category']:
    category_search = request.GET.get("category")
    searched_photos = Image.search_by_category(category_search)
    message = f"{category_search}"
    
    return render(request, 'search-results.html', {"message":message, "photos":searched_photos, "category_search":category_search})
  
  else:
    message = "You have not yet make a search"
    return render(request, 'search-results.html', {"message":message})
  