from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):

    # Two minimum values we need
    # classs meta represent minimum value
    # Metadata
    class Meta:
        # create model for Room based on metadata of class Room
        model = Room
        fields = '__all__' # Render all fields of the forms 
        exclude = ['host', 'participants']



