from django.test import TestCase
from .models import Image,Category,Location

# Create your tests here.
class CategoryTestCase(TestCase):
  # Set up method
  def setUp(self):
    self.new_category = Category(category = 'Travel')
    
  # Test instace
  def test_instance(self):
    self.assertTrue(isinstance(self.new_category, Category))
    
  # Test Save category method
  def test_save_method(self):
    self.new_category.save_category()
    categories = Category.objects.all()
    self.assertTrue(len(categories)==1)
    
  # Test Delete category method
  def test_delete_method(self):
    self.new_category.save_category()
    self.new_category.delete_category()
    categories = Category.objects.all()
    self.assertTrue(len(categories)==0)
    
  # Test Update Category Method
  def test_update_method(self):
    self.new_category.save_category()
    self.new_category.update_category(1)
    updated_category = Category.objects.filter(id = 1)
    self.assertTrue(self.new_category.category == 'Travel')
    
    
class LocationTestCase(TestCase):
  # Set up method
  def setUp(self):
    self.new_location = Location(location_name = 'Aboretum', country = 'Kenya', region = 'East Africa')
    
  # Test instace
  def test_instance(self):
    self.assertTrue(isinstance(self.new_location, Location))
    
  # Test Save category method
  def test_save_method(self):
    self.new_location.save_location()
    locations = Location.objects.all()
    self.assertTrue(len(locations)==1)