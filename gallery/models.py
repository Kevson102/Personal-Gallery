from django.db import models

# Create your models here.
class Location(models.Model):
  location_name = models.CharField(max_length=30)
  country = models.CharField(max_length=20)
  region = models.CharField(max_length=20)
  
  def __str__(self):
    return self.location_name
  
  # Save location method
  def save_location(self):
    self.save()
  
  # Delete location method
  def delete_location(self):
    self.delete()
  
class Category(models.Model):
  category = models.CharField(max_length= 15)
  
  def __str__(self):
    return self.category
  
  # Save category method
  def save_category(self):
    self.save()
    
  # Delete method
  def delete_category(self):
    self.delete()
    
  # Update method
  def update_category(self, var):
    Category.objects.filter(id = var).update(category = "Food")
  
class Image(models.Model):
  image = models.ImageField(upload_to = 'static/images/', blank=True)
  image_name = models.CharField(max_length=30)
  image_description = models.TextField()
  location = models.ForeignKey(Location, on_delete=models.CASCADE)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.image_name
  
  # Save image method
  def save_image(self):
    self.save()