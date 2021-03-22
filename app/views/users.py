from django.shortcuts import render
from app.models import User

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from app.serializers.users import UserRegisterSerializer


class UserView(APIView):

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)
    
    def post(self, request):
        """ 
        # Sample JSON
            {
                "name": "your name",
                "email": "test@admin.com",
                "password": "pass@123"
            }
        """
        data = request.data
        context = {}
        
        serializer = UserRegisterSerializer(data=data)
        
        if serializer.is_valid():
            try:
                user = User.objects.create(
                name=data['name'],
                email=data['email'],
                )
                user.set_password(data['password'])
                user.save()

                context['token'] = self.get_tokens_for_user(user)
                context['user-id'] = user.id
                return Response(context, status=200)
            except Exception as e:
                print(e)
                return Response('something went wrong! ' + str(e.args[0])) 
        return Response('400_BAD_REQUEST', status=400)