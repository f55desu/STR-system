from .models import Attendance, Schedule, Teacher_Subject, Criterion, Subject_Group, Grade, Teacher, Subject, Group, User
from .serializers import *

from rest_framework import generics

class APIAttendance(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class APISchedule(generics.ListCreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

class APIGrade(generics.ListCreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

class APISubject_group(generics.ListCreateAPIView):
    queryset = Subject_Group.objects.all()
    serializer_class = Subject_GroupSerializer

class APICriterion(generics.ListCreateAPIView):
    queryset = Criterion.objects.all()
    serializer_class = CriterionSerializer

class APITeacher_subj(generics.ListCreateAPIView):
    queryset = Teacher_Subject.objects.all()
    serializer_class = Teacher_SubjectSerializer

class APITeacher(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class APISubject(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class APIGroup(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class APIUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer