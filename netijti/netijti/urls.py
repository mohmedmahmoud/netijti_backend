

from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="NETIJTI",
        default_version='v1',
        description="Netijti est une application mobile développée en utilisant le framework Django et le framework REST API Django Rest Framework. Cette application permet aux utilisateurs de saisir des informations sur les résultats des matchs de football et d'afficher les statistiques des joueurs et des équipes.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="bouhmed1996@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)



router = routers.DefaultRouter()

urlpatterns = [
    path('', include('netijti_app.urls')),
    path("admin/", admin.site.urls),
    path('api-docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]
