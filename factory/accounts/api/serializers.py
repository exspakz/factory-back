from djoser.serializers import UserCreatePasswordRetypeSerializer

from accounts.models import UserProfile


class CustomUserCreateSerializer(UserCreatePasswordRetypeSerializer):
    def create(self, validated_data):
        user = super().create(validated_data)
        UserProfile.objects.create(user=user)
        return user
