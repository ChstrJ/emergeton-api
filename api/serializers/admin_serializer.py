from rest_framework import serializers 
from django.contrib.auth.hashers import make_password 
from .validator import must_contains_letters, letters_only, numbers_only, format_09
from ..models import Admin, User
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed

class UserSerializer(serializers.ModelSerializer):
     
    first_name = serializers.CharField(
        validators=[letters_only],
        max_length=50,
        min_length=3,
        required=True,
        error_messages={
            'blank': 'First name is required.'
        }
    )
    
    last_name = serializers.CharField(
        validators=[letters_only],
        max_length=50,
        min_length=3,
        required=True,
        error_messages={
            'blank': 'Last name is required.'
        }
    )
    
    email = serializers.EmailField(
        required=True,
        error_messages={
            'blank': 'Email is required.'
        }
    )

    password = serializers.CharField(
        required=True,
        write_only=True,
        max_length=20,
        min_length=8,
        error_messages={
            'blank': 'Password is required.'
        }
    )

    class Meta:
        model = User
        exclude = ('last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'groups', 'user_permissions')
        extra_kwargs = {
            'password': {'write_only': True}
        }

class AdminSerializer(serializers.ModelSerializer):
    
    user = UserSerializer()

    class Meta:
        model = Admin
        fields = ["user"]

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user_data['user_type'] = "admin"
        password = user_data.pop('password', None)  
        user = User(**user_data)

        if password:
            user.set_password(password)
        user.save()

        admin = Admin.objects.create(user=user, **validated_data)
        return admin

    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True) 
    password = serializers.CharField(required=True, write_only=True)
    

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        
        print(email, password)

        if not email or not password:
            raise serializers.ValidationError("Email and password are required.")
        
        request = self.context.get('request')
        user = authenticate(request, email=email, password=password)
        
        print(user)
        
        if not user:
            raise AuthenticationFailed("Invalid email or password.")
        
        attrs['user'] = user
        return attrs