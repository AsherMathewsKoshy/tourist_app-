from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DestinationViewSet
from . import views as dest_views
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib import admin
router = DefaultRouter()
router.register(r'destinations', DestinationViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Include the API routes
    path('register/', dest_views.register, name='register'),  # Registration page
    path('login/', dest_views.login_view, name='login'),  # Login page for the API
    path('destinations/', dest_views.destination_list, name='destination_list'),  # Destination list for web
    path('api/login/', obtain_auth_token, name='api_token_auth'),
    path('admin/', admin.site.urls),


]
