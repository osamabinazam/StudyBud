from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# Get rid of HttpResponse

# def home(reqeust):
#     return HttpResponse("Hello World, This is Home Page")

# def room(request):
#     return HttpResponse("This Root For Chatting and Discussion in StudyBud")

# Rendering Home template
def home(request):
    return render(request , 'home.html')
#Rendering Room template
def room(request):
    return render(request ,'room.html' )