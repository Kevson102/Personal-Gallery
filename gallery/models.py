from django.db import models

# Create your models here.
class Location(models.Model):
  location_name = models.CharField(max_length=30)
  country = models.CharField(max_length=20)
  region = models.CharField(max_length=20)
  
class Category(models.Model):
  category = models.CharField(max_length= 15)
  
  def __str__(self):
    return self.category
  
  # Save method
  def save_category(self):
    self.save()
  
class Image(models.Model):
  image = models.ImageField(upload_to = 'static/images/', blank=True)
  image_name = models.CharField(max_length=30)
  image_description = models.TextField()
  location = models.ForeignKey(Location, on_delete=models.CASCADE)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.image_name
  