from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response

from app.serializers.users import UserLoginSerializer
from app.serializers.advisor import AdvisorSerializer
from app.serializers.booking import AdvisorBookingSerializer

from app.models import Advisor, Booking

class SecondUserView(GenericViewSet, mixins.RetrieveModelMixin):
    
    def user_login(self, request):
        context = {}
        data = request.data
        email = data['email']
        password = data['password']
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            context['token'] = get_tokens_for_user(user)
            context['user-id'] = user.pk
            return Response(context, status=200)
        else:
            return Response('401_AUTHENTICATION_ERROR', status=401)
    
        return Response('400_BAD_REQUEST', status=400)

    # list advisor
    def get_list_advisor(self, request, user_id):
        obj = Advisor.objects.all()
        serializer = AdvisorSerializer(obj, many=True)

        return Response(serializer.data)

    def calls_booking(self, request, advisor_id, user_id):
        try:
            data = request.data
            advisor = Booking.objects.create(user_id=user_id, advisor_id=advisor_id, date_time=data['booking_time'])
            if advisor:
                return Response(f'Successfully Done! Books at {data["booking_time"]}', status=200)
            
        except Exception as e:
            print(e)
            return Response('Something went wrong!', status=400)

    def booked_calls(self, request, user_id):
        booking = Booking.objects.filter(user_id=user_id)
        serializer = AdvisorBookingSerializer(booking, many=True)
        return Response(serializer.data)


# pre-defined functions
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token)
