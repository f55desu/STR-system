# from dataclasses import fields
# from unittest.util import _MAX_LENGTH
from rest_framework import serializers
# from rest_framework.parsers import JSONParser
# from rest_framework.renderers import JSONRenderer
# import io

from .models import Attendance, Schedule, Teacher_Subject, Criterion, Subject_Group, Grade, Teacher, Subject, Group

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'

class Subject_GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject_Group
        fields = '__all__'

class CriterionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Criterion
        fields = '__all__'

class Teacher_SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher_Subject
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'