from django.db.models import query
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Image
from django.http import Http404, JsonResponse
from django.core import serializers
# Create your views here.
def home(request):
    images = Image.objects.all()
    return render(request, "index.html", {"title":"Home","images":images}) 

def get(request,id): 
    # if request.is_ajax():   
    # image_detail=Image.objects.all()
    # image_detail = get_object_or_404(Image, pk=id)

    image_detail=Image.objects.filter(id=id)
    print(id)
    # return JsonResponse({"users":image_detail})

    return JsonResponse({"users":list(image_detail.values())})
    # return HttpResponse(image_detail, content_type="application/json")

def search(request):
    if request.method=="POST":
        query = request.POST['query']
        image=Image.objects.filter(description=query)
        return render(request, "search.html", {"title":"Results","images":image}) 
    else:
        return redirect("home")
