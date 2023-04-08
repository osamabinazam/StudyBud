from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# Where databases are created
# creating classes that represent tables
# Row will be the instance of the class

class Topic (models.Model):
        name = models.CharField(max_length=200)

        def __str__(self):
                return self.name


# Room Table 
class Room(models.Model ):
        """All are column fileds"""
        # set relation to host or users
        host = models.ForeignKey(User, on_delete=models.SET_NULL , null=True)
        # set relations to room's topic
        topic = models.ForeignKey(Topic, on_delete=models.SET_NULL , null=True)
        name = models.CharField(max_length=200)
        description = models.TextField(null=True, blank=True)

        #Stores all users that are currently connected to room
        # participants =

        # Store activity timestamp every time we save
        update=models.DateTimeField(auto_now=True)
        # Stores time stamp when instance created first time
        created = models.DateTimeField(auto_now_add=True)

        class Meta:
                # ordering = ['update', 'created']               # ordering in ascending order
                ordering = ['-update', '-created']             # ordering in Descending Order

        def __str__(self) :
                return str(self.name)


class Message(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)

        # Setting relationship to room table. It will be one to many
        #if room is deleted then all children should be deleted
        room = models.ForeignKey(Room, on_delete=models.CASCADE)
        body = models.TextField()

        # Store activity timestamp every time we save
        update=models.DateTimeField(auto_now=True)

        # Stores time stamp when instance created first time
        created = models.DateTimeField(auto_now_add=True)

        def __str__(self):
                return self.body[0:50]
