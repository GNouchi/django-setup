from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
#  this page does not look at url at all but is called based on name of views.___ in app urls.py file

def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)
def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)
def create(request):
    return redirect('/')
def show(request,number):
    response= f"placeholder to display blog  {number}"
    return HttpResponse(response)
def edit(request,number):
    response= f"placeholder to edit blog {number}. "
    return HttpResponse(response)
def destroy(request,number):
    return redirect('/')


