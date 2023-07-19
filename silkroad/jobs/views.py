from rest_framework         import viewsets, permissions, status
from rest_framework.response    \
                            import Response
from rest_framework.decorators  \
                            import action

from .models                import Job
from .serializers           import JobSerializer
from applications.serializers \
                            import ApplicationSerializer
from applications.models    import Application
from users.permissions      import IsOwnerOrReadOnly

from django.db.models       import Q


class JobViewSet(viewsets.ModelViewSet):
    """
    A model view set for job.
    This is where applications are applied and listed.
    """
    queryset            = Job.objects.all()
    serializer_class    = JobSerializer
    permission_classes  = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]



    def get_queryset(self):
        """
        Displays Job data that are not deleted.
        """
        return Job.objects.filter(is_deleted=False)

    @action(detail=True)
    def apply(self, request, pk=None):
        applied_job = Job.objects.get(pk=pk)
        owner       = request.user

        if Application.objects.filter(Q(applied_job=applied_job) & ~Q(status=2)).exists():
            return Response("error", status=status.HTTP_400_BAD_REQUEST)
        if applied_job.owner == owner:
            return Response("error", status=status.HTTP_400_BAD_REQUEST)

        serializer = ApplicationSerializer(data=request.data)
        serializer.is_valid()
        serializer.save(applied_job=applied_job, owner=owner)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True)
    def applications(self, request, pk=None):
        applications    = Application.objects.filter(Q(applied_job=pk) & ~Q(status=2))
        serializers     = ApplicationSerializer(applications, many=True)

        return Response(serializers.data, status=status.HTTP_200_OK)



