from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Image,Location,Category

#Create your views here.
def image(request):
    image = Image.get_all()
    return render(request,"all_images/photo.html", {"image":image})
def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET .get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all_images/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all_images/search.html',{"message":message})

def detail(request,image_id):
    image = Image.objects.get(id = image_id)
    return render(request,"all_images/details.html", {"image":image})
def location(request,country):
    locate= location.objects.get(location=country)
    return render(request,"all_images/location.html",{"locate":locate})
        

