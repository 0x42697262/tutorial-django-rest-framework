from rest_framework             import viewsets

from django.contrib.auth.models import User
from .serializers               import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset            = User.objects.all()
    serializer_class    = UserSerializer

    def get_queryset(self):
        """
        Lists User that is active
        """
        return User.objects.filter(is_active=True)
