from rest_framework import serializers
from .models import * 


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        
        
class TravelNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelNews
        fields = '__all__'
