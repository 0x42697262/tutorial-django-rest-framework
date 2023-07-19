from rest_framework         import serializers

from .models                import Application


class ApplicationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Application model.
    """

    applied_job = serializers.PrimaryKeyRelatedField(read_only=True)
    owner       = serializers.CharField(read_only=True)
    status      = serializers.IntegerField(read_only=True)
    class Meta:
        model = Application
        fields = ['owner', 'status', 'applied_job']
