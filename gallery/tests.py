from django.test import TestCase
from .models import Category, Location,Image
# Create your tests here.

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

    def tearDown(self):
        Location.objects.all().delete()
        Category.objects.all().delete()
        Image.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))
        self.assertTrue(isinstance(self.new_category,Category))
        self.assertTrue(isinstance(self.new_location,Location))


        """Testing Location"""
    def update_location(self):
        name="Eldoret"
        updates=Location.update(name)
        self.assertEqual(name,"Eldoret")

    def delete_location(self):
        id=1
        Location.delete(id)
        loc = Location.objects.get(id)
        self.assertTrue(len(loc) == 0)

    """Testing Category"""
    def update_category(self):
        name="Tours"
        updates=Location.update(name)
        self.assertEqual(name,"Tours")


    def delete_location(self):
        id=1
        Category.delete(id)
        cat = Category.objects.get(id)
        self.assertTrue(len(cat) == 0)
#  def test_get_news_by_date(self):
#             test_date = '2017-03-17'
#             date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
#             news_by_date = Article.days_news(date)
#             self.assertTrue(len(news_by_date) == 0)