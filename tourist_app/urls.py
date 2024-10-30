from django.contrib import admin
from django.urls import path, include
from destinations import views as dest_views
from django.conf import settings
from django.conf.urls.static import static
from destinations.views import logout_view
from django.urls import path, include
from destinations import views as dest_views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'destinations', dest_views.DestinationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('destinations.urls')),  # API endpoints for CRUD
    path('register/', dest_views.register, name='register'),
    path('login/', dest_views.login_view, name='login'),  # Web login
    path('destinations/', dest_views.destination_list, name='destination_list'),
    path('api/login/', dest_views.login_view, name='api_login'),  # Custom API login
    path('api/logout/', logout_view, name='logout'),
    path('destinations/edit/<int:pk>/', dest_views.edit_destination, name='edit_destination'), 
    path('destinations/delete/<int:pk>/', dest_views.delete_destination, name='delete_destination'), 
    path('destinationeditor/', dest_views.destination_editor, name='destination_editor'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
