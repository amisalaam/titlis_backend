from django.urls import path
from .views import *


urlpatterns = [
    path('get/all/posts/', PostView.as_view(), name='posts'),
]

