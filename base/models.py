from django.db import models

# Create your models here.
# Where databases are created
# creating classes that represent tables
# Row will be the instance of the class

# Room Table 
class Room(models.Model):
        #host =
        #topic = 
        name = models.CharField(max_length=200)
        description = models.TextField(null=True, blank=True)

        #Stores all users that are currently connected to room
        # participants =

        # Store activity timestamp every time we save
        update=models.DateTimeField(auto_now=True)
        # Stores time stamp when instance created first time
        created = models.DateTimeField(auto_now_add=True)

        def __str__(self) :
                return str(self.name)

