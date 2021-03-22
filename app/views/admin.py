from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from app.serializers.advisor import AdvisorSerializer

class AdminView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
    
    def post(self, request):
        data = request.data
        serializer = AdvisorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response('successfully added!', status=200)
        
        return Response('Please fill valid data!', status=400)