from django.shortcuts import render
from rest_framework import generics
from .models import Teacher, Student
from .serializers import TeacherSerializer, StudentSerializer
from rest_framework import viewsets


# Create your views here.
class TeacherListCreateView(viewsets.ModelViewSet):
    """View to list and create teachers."""
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    
class StudentListCreateView(viewsets.ModelViewSet):
    """View to list and create students."""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer    