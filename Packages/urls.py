from django.urls import path
from .views import GetAllPackages, PackagePlans

urlpatterns = [
    path('get/all/packages/', GetAllPackages.as_view(), name='packages'),
    path('get/package/plans/', PackagePlans.as_view(), name='package_plans'),
]
