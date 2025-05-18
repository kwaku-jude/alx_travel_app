from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def home(request):
    return Response({
        "message": "Welcome to ALX Travel App API - Listings Home",
        "status": "success"
    })
