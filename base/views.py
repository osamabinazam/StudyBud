from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# Get rid of HttpResponse

# def home(reqeust):
#     return HttpResponse("Hello World, This is Home Page")

# def room(request):
#     return HttpResponse("This Root For Chatting and Discussion in StudyBud")

# list of client in rooms
rooms = [
     {'id':1 , 'name' : 'Lets learn python'},
     {'id':2 , 'name': 'Design with me'},
     {'id':3 , 'name':'Frontend Developers' }
]



# Rendering Home template
def home(request):
    context = {'rooms':rooms}
    return render(request , 'base/home.html', context)
#Rendering Room template
def room(request, pk ):
    return render(request ,'base/room.html' )