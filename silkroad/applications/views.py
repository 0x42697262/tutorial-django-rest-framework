from rest_framework     import viewsets, status, permissions
from rest_framework.response \
                        import Response
from rest_framework.decorators \
                        import action

from django.shortcuts   import get_object_or_404

from .models            import Application
from .serializers       import ApplicationSerializer
from users.permissions  import IsOwnerOrReadOnly
from jobs.models        import Job

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset            = Application.objects.all()
    serializer_class    = ApplicationSerializer
    permission_classes  = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    @action(detail=True)
    def accept(self, request, **kwargs):
        return self.set_status(request, status=1, **kwargs)

    @action(detail=True)
    def decline(self, request, **kwargs):
        return self.set_status(request, status=-1, **kwargs)

    @action(detail=True)
    def withdraw(self, request, **kwargs):
        return self.set_status(request, status=2, **kwargs)
    

    def set_status(self, request, **kwargs):
        job_id          = kwargs.get('job_id')
        application_id  = kwargs.get('pk')
        new_status      = kwargs.get('status')
        applied_job     = Job.objects.get(pk=job_id)
        application     = get_object_or_404(Application, pk=application_id)

        match new_status:
            # withdraw
            case 2:
                if application.owner != request.user:
                    return Response({"Not the job applicant."}, status=status.HTTP_400_BAD_REQUEST)
            case -1|1:
                if applied_job.owner != request.user:
                    return Response({"Not the creator."}, status=status.HTTP_400_BAD_REQUEST)


        application.status  = new_status
        application.save()

        serializer      = ApplicationSerializer(application)

        return Response(serializer.data, status=status.HTTP_200_OK)
