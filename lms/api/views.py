from django.shortcuts import render
from rest_framework import generics
from .models import Teacher, Student,Profile
from .serializers import TeacherSerializer, StudentSerializer, RegisterSerializer, loginSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.
class TeacherListCreateView(viewsets.ModelViewSet):
    """View to list and create teachers."""
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    
class StudentListCreateView(viewsets.ModelViewSet):
    """View to list and create students."""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer  

class RegisterView(viewsets.ModelViewSet):
    """User registration view."""
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(APIView):
    """Login view using phone and password."""

    def post(self, request):
        serializer = loginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.validated_data['phone']
        password = serializer.validated_data['password']

        try:
            profile = Profile.objects.get(phone=phone)
            user = profile.user
        except Profile.DoesNotExist:
            return Response({'error': 'Invalid phone or password'}, status=status.HTTP_400_BAD_REQUEST)

        if not user.check_password(password):
            return Response({'error': 'Invalid phone or password'}, status=status.HTTP_400_BAD_REQUEST)

        tokens = get_tokens_for_user(user)
        return Response({
            'message': 'Login successful',
            'user_id': user.id,
            'username': user.username,
            'tokens': tokens
        })

def get_tokens_for_user(user):
    """Helper to get JWT tokens for a user."""
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }