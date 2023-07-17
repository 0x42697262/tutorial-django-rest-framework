from rest_framework         import viewsets

from .models                import Application
from .serializers           import ApplicationSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset            = Application.objects.all()
    serializer_class    = ApplicationSerializer

    def get_queryset(self):
        """
        Displays Application data that are not deleted.
        """
        return Application.objects.filter(is_deleted=False)
