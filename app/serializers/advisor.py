from rest_framework import serializers
from app.models import Advisor

class AdvisorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Advisor
        fields = ['id', 'name', 'photo_url']
        