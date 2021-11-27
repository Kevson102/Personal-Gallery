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
    
  # Delete image method
  def delete_image(self):
    self.delete()
    
  # Update image
  @classmethod
  def update_image(cls, id, image, image_name, image_description, location, category):
    updated_image = cls.objects.filter(id = id).update(image=image, image_name = image_name, image_description=image_description, location = location, category=category)
    return updated_image
  
  # Get all images
  @classmethod
  def get_all_images(cls):
    all_images = cls.objects.all()
    return all_images
  
  # Get image by id
  @classmethod
  def get_image_by_id(cls, id):
    searched_image = Image.objects.filter(id = id).all()
    return searched_image
  
  # Search image by category
  @classmethod
  def search_by_category(cls, search_phrase):
    found_images = cls.objects.filter(category=search_phrase)
    return found_images