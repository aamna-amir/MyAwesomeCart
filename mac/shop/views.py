from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "shop/index.html")

def about(request):
    return HttpResponse("About US")

def contact(request):
    return HttpResponse("Contact US")

def tracker(request):
    return HttpResponse("Tracker")

def search(request):
    return HttpResponse("Search")

def prodView(request):
    return HttpResponse("Product View")

def checkout(request):
    return HttpResponse("checkout")