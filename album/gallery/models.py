from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.ImageField(upload_to = 'images/', default='images/default.jpg')
    description = models.TextField()
    editor = models.ForeignKey('Editor', on_delete=models.CASCADE)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE) 
    pub_date = models.DateTimeField(auto_now_add=True)

    # @classmethod
    # def save_image(cls):
    #     image = cls.objects.create(id = id)
    #     image.name = 'Pear'
    #     return image.save()

    # @classmethod
    # def days_news(cls,date):
    #     news = cls.objects.filter(pub_date__date = date)
    #     return news
    # def save_image():
    #      - Save an image to the database.
    # def delete_image():
    #     return - Delete image from the database.
    # def update_image():
    #     return - Update image in the database.
    # def get_image_by_id(id):
    #     return - Allows us to get an image using its ID.
    # def search_image(category):
    #      - Allows us to search for an image using its category.
    # def filter_by_location(location):

    def __str__(self):
        return self.description

class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)

    def __str__(self):
        return self.first_name+" "+self.last_name

class Location(models.Model):
    name = models.CharField(max_length =30)

    class Meta:
        verbose_name_plural='Locations'
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length =30)

    class Meta:
        verbose_name_plural='Categories'
    def __str__ (self):
        return self.name