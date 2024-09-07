from rest_framework import serializers
from .models import *

class AttendeeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Attendee
        fields = ('__all__')