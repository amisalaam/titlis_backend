from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Package, Plans
from .serializers import PackageSerializer, PlansSerializer

# Create your views here.

class GetAllPackages(APIView):
    
    def get(self, request):
        packages = Package.objects.all()
        serializer = PackageSerializer(packages, many=True)
        return Response(serializer.data)


class PackagePlans(APIView):
    
    def get(self,request):
        package_id = request.GET.get('package_id')
        
        plans = Plans.objects.filter(package=package_id)
        serializer = PlansSerializer(plans, many=True)
        return Response(serializer.data)    
        
        

