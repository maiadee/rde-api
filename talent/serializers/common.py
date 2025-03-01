from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from ..models import Talent, TalentImage

class TalentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TalentImage
        fields = ["id", "image"]

class TalentSerializer(ModelSerializer):
    profile_picture = serializers.ImageField(required=False)  # Ensure profile image is included
    images = TalentImageSerializer(many=True, read_only=True)  # Include multiple images

    class Meta:
        model = Talent
        fields = '__all__'

class TalentNameSerializer(ModelSerializer):
    class Meta:
        model = Talent
        fields = ['id', 'name']