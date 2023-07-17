from rest_framework         import serializers

from .models                import Job
from django.contrib.auth.models     import User

class JobSerializer(serializers.ModelSerializer):
    """
    Serializer for the Job model.
    """

    # Make the owner field not required
    owner = serializers.PrimaryKeyRelatedField(
            queryset=User.objects.all(),
            required=False)

    class Meta:
        model = Job
        fields = ['owner', 'title', 'description']

    def create(self, validated_data):
        """
        Custom logic for creating a job
        """
        return Job.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Custom logic for updating a job
        Update the instance with the validated data and save it
        """
        instance.title          = validated_data.get('title', instance.title)
        instance.description    = validated_data.get('description', instance.description)
        instance.owner          = validated_data.get('owner', instance.owner)
        instance.save()

        return instance
    
    def perform_destroy(self, instance):
        """
        Custom logic for deleting a job
        Sets the is_deleted field to True
        """
        instance.is_deleted = True
        instance.save()
