from rest_framework.serializers import ModelSerializer
from ..models import Talent

class TalentSerializer(ModelSerializer):
    class Meta:
        model = Talent
        fields = '__all__'

class TalentNameSerializer(ModelSerializer):
    class Meta:
        model = Talent
        fields = ['name']