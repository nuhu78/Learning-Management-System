from rest_framework import serializers

from .models import Teacher, Student

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'name', 'email', 'subject', 'is_active']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'enrollment_date', 'is_active', 'roll_number']
