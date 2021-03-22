from rest_framework import serializers
from app.models import Booking, Advisor

class BookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'date_time']

class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisor
        fields = ['id', 'name', 'photo_url']

class AdvisorBookingSerializer(serializers.ModelSerializer):
    advisor = AdvisorSerializer(read_only=True)
    class Meta:
        model = Booking
        fields = ['advisor', 'date_time', 'id']