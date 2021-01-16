from rest_framework import serializers

from .models import LightSample

class LightSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ('id','name','light_type','price')
        model = LightSample