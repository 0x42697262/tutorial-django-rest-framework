from rest_framework                 import serializers

from django.contrib.auth.models     import User
from django.contrib.auth.hashers    import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model           = User
        fields          = ['username', 'email', 'password']
        extra_kwargs    = {
                'password' : {
                    'write_only' : True,
                    },
                }
    def update(self, instance, validated_data):
        """
        Custom logic for updating a user
        """


        instance.username   = validated_data.get('username',    instance.username)
        instance.email      = validated_data.get('email',       instance.email)
        
        # Encrypt the password if it's included in the validated data
        password            = validated_data.get('password')
        if password:
            instance.password = make_password(password)

        instance.save()

        return instance
