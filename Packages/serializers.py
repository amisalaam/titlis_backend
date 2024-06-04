from rest_framework import serializers
from .models import Package,Plans


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ['id', 'name', 'image', 'description','continent', 'created_at', 'updated_at']
        

class PlansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plans
        fields = '__all__'