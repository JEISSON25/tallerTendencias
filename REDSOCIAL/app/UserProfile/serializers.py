from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile

class UserSerializer(serializers.ModelSerializer):
    profile_picture = serializers.ImageField(required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile_picture']

    def create(self, validated_data):
        profile_picture = validated_data.pop('profile_picture', None)
        user = User.objects.create(**validated_data)
        if profile_picture:
            UserProfile.objects.create(user=user, profile_picture=profile_picture)
        return user

    def update(self, instance, validated_data):
        profile_picture = validated_data.pop('profile_picture', None)
        instance = super().update(instance, validated_data)
        profile = UserProfile.objects.filter(user=instance).first()
        if profile:
            if profile_picture:
                profile.profile_picture = profile_picture
                profile.save()
        return instance
