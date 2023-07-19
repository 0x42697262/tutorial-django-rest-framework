from rest_framework             import viewsets, status
from rest_framework.response    import Response

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


    def create(self, request, *args, **kwargs):
        serializer  = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user        = User.objects.create_user(**serializer.validated_data)

        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
    
