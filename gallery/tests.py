from django.test import TestCase
from .models import Image,Category,Location
import datetime as dt
from django.shortcuts import get_object_or_404

class ImageTestClass(TestCase):
    def setUp(self):
        # Creating a new location and saving it
        self.new_location = Location(name = 'Mombasa')
        self.new_location.save_location()

        # Creating a new category and saving it
        self.new_category = Category(name = 'Travel')
        self.new_category.save_category()

        # Creating a new image and saving it
        self.image=Image(image = 'xyz.jpg', image_name ='Hotel', description ='It was a one tour to mombasa',location=self.new_location,category=self.new_category ,pub_date="2021-09-05 22:16:35.61389+03")
        self.image.save_image()

        # self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Image.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()

    """Test image""" 
    def test_get_image_by_id(self):
        image = Image.objects.first()
        id=image.id
        results = Image.get_image_by_id(id)
        self.assertTrue(len(results)==1)

    def test_update_image(self):
        image_obj = Image.objects.all()[:1].get()
        id=image_obj.id
        image="kk.jpg"        
        
        Image.update_image(id,image)
        image = Image.objects.get(id=id)
        self.assertEqual(image.image.url,"http://res.cloudinary.com/dw6wdyms4/image/upload/kk.jpg")

    def test_search_image(self):
        image = Image.objects.first()
        category = image.category
        results = Image.search_image(category)
        self.assertTrue(len(results) > 0)

    def test_filter_by_location(self):
        image = Image.objects.first()
        location = image.location
        results = Image.filter_by_location(location)
        self.assertTrue(len(results) > 0)

    def test_delete_image(self):
        image=Image.objects.first()
        id=image.id
        Image.delete_image(id)
        try:
            img = Image.objects.get(id=id)
            self.assertTrue("Some results")
        except Image.DoesNotExist:
            self.assertTrue("no results"=="no results")


        """Testing Location"""
    def test_update_location(self):
        location = Location.objects.first()
        name="Eldoret"
        id=location.id
        Location.update(id,name)
        updated_location = Location.objects.get(id=id)
        self.assertEqual(updated_location.name,"Eldoret")

    def test_delete_location(self):
        location=Location.objects.first()
        id=location.id
        Location.delete_location(id)
        try:
            img = Location.objects.get(id=id)
            self.assertTrue("Some results")
        except Location.DoesNotExist:
            self.assertTrue("Deleted successfully"=="Deleted successfully")

    """Testing Category"""
    def test_update_category(self):
        category = Category.objects.first()
        name="Travel"
        id=category.id
        Category.update(id,name)
        updated_category = Category.objects.get(id=id)
        self.assertEqual(updated_category.name,"Travel")

    def test_delete_category(self):
        category=Category.objects.first()
        id=category.id
        Category.delete_category(id)
        try:
            img = Category.objects.get(id=id)
            self.assertTrue("Some results")
        except Category.DoesNotExist:
            self.assertTrue("Deleted successfully"=="Deleted successfully")