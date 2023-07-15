from rest_framework         import serializers

from .models                import Application
from jobs.serializers       import JobSerializer


class ApplicationSerializer(serializers.ModelSerializer):
    applied_job = JobSerializer
    class Meta:
        model = Application
        fields = ['owner', 'status', 'applied_job']
