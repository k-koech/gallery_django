from django.db.models import query
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Category, Image, Location
from django.http import Http404, JsonResponse
from django.core import serializers
import json


# Create your views here.
def home(request):
    images = Image.objects.all()
    category=Category.objects.all()
    location = Location.objects.all()

    e_images = Image.objects.filter(location="2")
    m_images = Image.objects.filter(location="1")
    n_images = Image.objects.filter(location="3")
    return render(request, "index.html", {"title":"Home","e_images":e_images, "m_images":m_images, "n_images":n_images,"categories":category,"location":location,"images":images}) 

def get(request,id): 
    image_detail=Image.objects.get(id=id)
    
    image_dict={}
    image_dict['id']=image_detail.id
    image_dict['image']=image_detail.image.url
    image_dict['description']=image_detail.description
    image_dict['image_name']=image_detail.image_name
    image_dict['location']=image_detail.location.name
    image_dict['category']=image_detail.category.name
    j_object=json.dumps(image_dict)
    return JsonResponse({"users":j_object})

def search(request):
    if request.method=="POST":
        query = request.POST['category']
        image=Image.objects.filter(category=query)
        category=Category.objects.get(id=query)
        header=category.name
        return render(request, "search.html", {"title":"Results","images":image, "header":header}) 
    else:
        return redirect("home")
