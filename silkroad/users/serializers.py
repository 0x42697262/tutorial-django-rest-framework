
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
        Encrypt the password if it's included in the validated data
        """
        password = validated_data.get('password')
        if password:
            validated_data['password'] = make_password(password)
        return super().update(instance, validated_data)
