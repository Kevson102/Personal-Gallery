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
    
  # Test Delete category method
  def test_delete_method(self):
    self.new_location.save_location()
    self.new_location.delete_location()
    locations = Location.objects.all()
    self.assertTrue(len(locations)==0)
    
class ImageTestCase(TestCase):
  # Set up method for the test case.
  def setUp(self):
    # Create and save a category instance for the test
    self.new_category = Category(category = 'Travel')
    self.new_category.save_category()
    
    # Create and save a location instance
    self.new_location = Location(location_name = 'Aboretum', country = 'Kenya', region = 'East Africa')
    self.new_location.save_location()
    
    # Create and save an image instance
    self.image = Image(1, 'image location', 'hiking', 'hiking mount everest', self.new_location.id, self.new_category.id)
    self.image.save()
    
  def tearDown(self):
    Category.objects.all().delete()
    Location.objects.all().delete()
    Image.objects.all().delete()
    
  # Test instance
  def test_instance(self):
    self.assertTrue(isinstance(self.image, Image))
  
  # Test save image method
  def test_save_image(self):
    self.image.save_image()
    images = Image.objects.all()
    self.assertTrue(len(images)==1)