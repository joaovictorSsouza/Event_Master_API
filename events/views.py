from rest_framework import viewsets, generics
from .models import Event
from .serializers import EventSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

class EventViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]

    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserViewSet(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    






