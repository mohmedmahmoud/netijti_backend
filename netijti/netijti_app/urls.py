from django.urls import include, path
from rest_framework import routers
from .views import SectorViewSet, ResultViewSet

router = routers.DefaultRouter()
router.register(r'sectors', SectorViewSet)
router.register(r'results', ResultViewSet)

urlpatterns = [
  
    path('api/', include(router.urls)),
   
]