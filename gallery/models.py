from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class Image(models.Model):
    image = CloudinaryField('image')
    image_name= models.CharField(max_length =30)
    description = models.TextField()
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE) 
    pub_date = models.DateTimeField(auto_now_add=True)

    def save_image(self):
        return self.save()

    # @classmethod
    # def days_news(cls,date):
    #     news = cls.objects.filter(pub_date__date = date)
    #     return news
    @classmethod
    def delete_image(cls):
        del_image = cls.objects.get(id).delete()
        return del_image
    
    @classmethod
    def update_image(cls, id,image):
        get_img=cls.objects.get(id=id)
        get_img.image=image
        return get_img.save()

    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.filter(id = id)
        return image

    @classmethod
    def search_image(cls,category):
        image = cls.objects.filter(category = category)
        return image
    
    @classmethod
    def filter_by_location(cls,location):
        image = cls.objects.filter(location = location)
        return image

    def __str__(self):
        return self.description


class Location(models.Model):
    name = models.CharField(max_length =30)

    def save_location(self):
        self.save()

    @classmethod
    def update(cls,name):
        location= cls.objects.first()
        location.name= name
        return location.save()

    @classmethod
    def delete(cls,id):
        del_location = cls.objects.get(id).delete()
        return del_location

    class Meta:
        verbose_name_plural='Locations'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length =30)

    class Meta:
        verbose_name_plural='Categories'

    def save_category(self):
        self.save()

    @classmethod
    def update(cls,name):
        category= cls.objects.first()
        category.name= name
        return category.save()

    @classmethod
    def delete(cls,id):
        del_category = cls.objects.get(id).delete()
        return del_category


    def __str__ (self):
        return self.name