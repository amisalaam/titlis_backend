from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post, TravelNews
from .serializers import PostSerializer, TravelNewsSerializer

class PostView(APIView):
    def get(self, request):
        feed = Post.objects.all()
        serializer = PostSerializer(feed, many=True)
        
        response_data = {
            'data': serializer.data,
            'message': "Feed fetched successfully"
        }

        return Response(response_data, status=status.HTTP_200_OK)


class TravelNewsView(APIView):
    def get(self,request):
        news = TravelNews.objects.all()
        serilizers = TravelNewsSerializer(news, many=True)
        
        response_data = {
            'data': serilizers.data,
            'message': "News fetched successfully"
        } 

        return Response(response_data, status=status.HTTP_200_OK)