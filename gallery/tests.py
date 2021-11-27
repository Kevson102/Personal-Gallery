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