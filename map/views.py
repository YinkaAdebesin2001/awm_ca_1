from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.gis.geos import Point
from django.shortcuts import render

from .models import Location

# Create your views here.

 

def map_view(request):

    locations = Location.objects.all()

    return render(request, 'map/map.html', {'locations': locations})

def update_location(request):   
    # Ensure the user is authenticated
    if not request.user.is_authenticated:
        return JsonResponse({'success': False, 'error': 'User not authenticated'}, status=401)

    # Check if the request method is POST
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        # Validate latitude and longitude values
        if latitude is None or longitude is None:
            return JsonResponse({'success': False, 'error': 'Latitude or longitude missing'}, status=400)

        # Try to update the user's profile location
        try:
            # Assuming the profile exists and has a location field
            user_profile = request.user.profile  # Adjust if 'profile' is a custom attribute
            user_profile.location = Point(float(longitude), float(latitude))
            user_profile.save()
            return JsonResponse({'success': True})

        except Exception as e:
            # Handle any errors
            return JsonResponse({'success': False, 'error': str(e)}, status=500)

    # If the request method isn't POST, return success False
    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=405)