from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, UserViewSet

router = DefaultRouter()
router.register(r'eventos', EventViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('cadastro/', UserViewSet.as_view(), name='cadastro-usuario')
]
