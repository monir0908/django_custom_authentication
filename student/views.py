from student.serializers import StudentResigtrationSerializer, StudentLoginSerializer
from student.models import Student
from rest_framework import generics, filters
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from student.models import Student



class StudentRegistration(APIView):
    permission_classes = (AllowAny,)
    serializer_class = StudentResigtrationSerializer

    def post(self, request):      
        
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class StudentLoginView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = StudentLoginSerializer

    
    def post(self, request):   
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)          