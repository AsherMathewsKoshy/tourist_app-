from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Destination
from .serializers import DestinationSerializer
from rest_framework.permissions import IsAuthenticated

class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    permission_classes = [IsAuthenticated]

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from rest_framework.authtoken.models import Token

# Registration view
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        Token.objects.create(user=user)
        return redirect('login')
    return render(request, 'destinations/register.html')

from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@csrf_exempt  # Disable CSRF for simplicity; remove for production
@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    # Authenticate the user
    user = authenticate(username=username, password=password)
    
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)  # Return the token on success
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)




from django.shortcuts import render
from .models import Destination
def destination_list(request):
    query = request.GET.get('search', '')  # Get the search query from the request
    if query:
        destinations = Destination.objects.filter(place_name__icontains=query)  # Filter based on the search query
    else:
        destinations = Destination.objects.all() 
    return render(request, 'destination_list.html', {'destinations': destinations})

from django.contrib import admin
from .models import Destination

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('place_name', 'country', 'state', 'district')  # Add other fields as needed
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
def logout_view(request):
    try:
        token = request.auth  # Get the token from the request
        token.delete()  # Delete the token from the database
        return Response({'success': 'Logged out successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from .models import Destination
from .serializers import DestinationSerializer
from rest_framework.permissions import IsAuthenticated
def edit_destination(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    if request.method == 'POST':
        destination.place_name = request.POST['place_name']
        destination.weather = request.POST['weather']
        destination.state = request.POST['state']
        destination.district = request.POST['district']
        destination.google_map_link = request.POST['google_map_link']
        destination.description = request.POST['description']
        destination.save()
        return redirect('destination_list')
    return render(request, 'edit_destination.html', {'destination': destination})

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from rest_framework import viewsets
from .models import Destination
from .serializers import DestinationSerializer
from rest_framework.permissions import IsAuthenticated
def delete_destination(request, pk):
    destination = get_object_or_404(Destination, pk=pk)

    # Optional: Check if the user is authenticated and authorized to delete
    if not request.user.is_authenticated:
        return HttpResponseForbidden("You are not allowed to delete this destination.")

    if request.method == 'POST':
        destination.delete()
        return redirect('destination_list')

    return render(request, 'delete_destination.html', {'destination': destination})

def destination_editor(request):
    destinations = Destination.objects.all()
    return render(request, 'destinations/destination_editor.html', {'destinations': destinations})