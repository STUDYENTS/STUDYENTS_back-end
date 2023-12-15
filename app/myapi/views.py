from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import render
from django.http import HttpResponse
import os

from .serializers import HeroSerializer, CourseSerializer, ModuleSerializer, LessonSerializer, TestSerializer, \
    TaskSerializer, AnswerSerializer
from .models import Hero, Course, Module, Lesson, Test, Task, Answer


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer
# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by('title')
    serializer_class = CourseSerializer

class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all().order_by('title')
    serializer_class = ModuleSerializer


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all().order_by('title')
    serializer_class = LessonSerializer

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all().order_by('title')
    serializer_class = TestSerializer



class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('question')
    serializer_class = TaskSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all().order_by('answer')
    serializer_class = AnswerSerializer

def theory_view_function(request, filename):
    file_path = os.path.join('../app/theory_files', filename)
    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="{filename}"'
        return response

def images_view_function(request, filename):
    file_path = os.path.join('../app/images_files', filename)
    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="{filename}"'
        return response
