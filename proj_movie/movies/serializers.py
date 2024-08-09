from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    access_token = serializers.CharField(read_only=True)
    username = serializers.CharField(write_only=True,
                                     required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'access_token')

    def generate_token(self):
        token_pair=TokenObtainPairSerializer(data={
            'username': self.initial_data['username'],
            'password': self.initial_data['password'],
        })
        try:
            token_pair.is_valid(raise_exception=True)
        except Exception as e:
            return {"message":str(e)}
        return {"access_token":token_pair.validated_data}

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        token_data=self.generate_token()
        access_token = token_data.get('access_token', {}).get("access") 
        return {"access_token":access_token}
