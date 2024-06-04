
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import Post
# Create your views here.


class PostView(APIView):
    def get(self,request):
        feed = Post.objects.all()
        serializer = PostSerializer(feed, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK,message="Feed fetched successfully")
        
        
        