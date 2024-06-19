from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.hashers import make_password
from django.conf import settings

class UserSerializer(serializers.ModelSerializer):
    profile_picture_url = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def get_profile_picture_url(self, obj):
        if obj.profile_picture:
            return self.context['request'].build_absolute_uri(obj.profile_picture.url)
        return None

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            name=validated_data.get('name'),
            address=validated_data.get('address'),
            profile_picture=validated_data.get('profile_picture')
        )
        user.password = make_password(validated_data['password'])
        user.save()
        return user
