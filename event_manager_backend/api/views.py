from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Event
from .serializers import EventSerializer


@api_view(['GET'])
def health(request):
    return Response({"message": "Server is up!"})


# PUBLIC_INTERFACE
class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint to manage events.
    Provides create, update, list, and retrieve functionality for Event objects.
    """
    queryset = Event.objects.all().order_by('-start_time')
    serializer_class = EventSerializer
    permission_classes = [AllowAny]
