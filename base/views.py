from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room, Topic
from .forms import RoomForm
from django.db.models import Q
# Create your views here.


# Get rid of HttpResponse

# def home(reqeust):
#     return HttpResponse("Hello World, This is Home Page")

# def room(request):
#     return HttpResponse("This Root For Chatting and Discussion in StudyBud")

# Rendering Home template
def home(request):
    q= request.GET.get('q') if request.GET.get('q') != None else ''
    #Adding filters to search bar and browse topic
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
        )

    topics = Topic.objects.all()
    room_count = rooms.count()
    context = {'rooms':rooms, 'topics':topics , 'room_count':room_count}
    return render(request , 'base/home.html', context )
#Rendering Room template
def room(request, pk ):
    return render(request ,'base/room.html' )

#Creating room
def createRoom (request):
    form = RoomForm()
    # Printing form values
    if request.method == 'POST':
        # for key, value in request.POST.items():
        #     print(key , " : " , value)
        form = RoomForm(request.POST)       # Passing request ot RoomForm that knows all about form
        if form.is_valid():
            form.save()                     # if data is valid then sent to db
            return redirect('home')         #redirect user to homepage
        else:
            print("Data is Not valid in POST request")
    else:
        print("Error !, Expect POST request but didn't get it")
    context = {'form':form}
    return render(request,'base/room_form.html', context)

# Updating room
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method =='POST':
        form = RoomForm(request.POST, instance=room )
        if form.is_valid:
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'base/room_form.html', context)


#Delete Room 
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    print("Room is : " , room)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'object':room})

# Bootstrap form submission
# def submit_boot(request):

#     if request.method == 'POST':
#         print("Connected to Frorm")
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         print("Name is : ",request.POST.get('name'))
#         print("Email is : ",request.POST.get('email'))

#         # validating form
#         if not name:
#             return render(request, 'base/boot.html', {'error_message': 'Please enter a name'})
#         elif not email:
#             return render(request, 'base/boot.html', {'error_message': 'Please enter an email'})
#         else:
#             print("No one Ran")
       
#     context ={}
#     return render(request, 'base/boot.html', context)