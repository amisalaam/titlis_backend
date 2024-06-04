from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer

class PostView(APIView):
    def get(self, request):
        feed = Post.objects.all()
        serializer = PostSerializer(feed, many=True)
        
        response_data = {
            'data': serializer.data,
            'message': "Feed fetched successfully"
        }

        return Response(response_data, status=status.HTTP_200_OK)
