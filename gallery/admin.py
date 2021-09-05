from django.contrib import admin
from .models import Editor, Location, Category, Image

"""
    Adding models to an array
"""
models=[Editor, Location, Category, Image]

# Register your models here.
for model in models:
    admin.site.register(model)


"""
    Editing admin page
"""
admin.site.site_header = "SnapShot Admin"
admin.site.site_title = "SnapShot Admin Portal"
admin.site.index_title = "SnapShot Portal"