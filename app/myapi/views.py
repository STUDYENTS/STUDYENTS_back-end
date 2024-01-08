from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import render
from django.http import HttpResponse, Http404
import os
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Module


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

# Пример заголовков CORS для Django
from django.http import HttpResponse

def video_view_function(request, filename):
    file_path = os.path.join('../app/video', filename)
    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='video/mp4')
        response['Content-Disposition'] = f'inline; filename="{filename}"'
        response['Access-Control-Allow-Origin'] = '*'  # Разрешить запросы с любого домена
        response['Access-Control-Allow-Methods'] = 'GET'  # Разрешить только GET-запросы
        return response


def theory_view_function(request, filename):
    file_path = os.path.join('../app/theory_files', filename)
    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="{filename}"'
        return response

def images_view_function(request, filename):
    file_path = os.path.join('../app/images_course', filename)
    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='image/jpg')
        response['Content-Disposition'] = f'inline; filename="{filename}"'
        return response
def images_course_view_function(request, filename):
    file_path = os.path.join('../app/img_course', filename)
    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='image/jpg')
        response['Content-Disposition'] = f'inline; filename="{filename}"'
        return response


def serialize_your_modules_function(modules):
    pass


from django.shortcuts import get_object_or_404


from django.shortcuts import get_object_or_404

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Module
from .serializers import ModuleSerializer

@api_view(['GET'])
def modules_for_course(request, course_id):
    try:
        # Извлекаем объект курса по его URL
        course = get_object_or_404(Course, id=course_id)
        # Фильтрация модулей по курсу
        course_modules = Module.objects.filter(course=course)
        # Проверка наличия модулей
        if not course_modules.exists():
            return Response({"error": "Modules not found for the specified course_id."},
                            status=status.HTTP_404_NOT_FOUND)

        # Сериализация и возврат данных
        serialized_modules = ModuleSerializer(course_modules, many=True, context={'request': request})
        return Response(serialized_modules.data)
    except Course.DoesNotExist:
        return Response({"error": "Course does not exist."},
                        status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def lessons_for_module(request, module_id):
    try:
        # Извлекаем объект модуля по его ID
        module = get_object_or_404(Module, id=module_id)
        # Фильтрация уроков по модулю
        module_lessons = Lesson.objects.filter(module=module)
        # Проверка наличия уроков
        if not module_lessons.exists():
            return Response({"error": "Lessons not found for the specified module_id."},
                            status=status.HTTP_404_NOT_FOUND)

        # Сериализация и возврат данных
        serialized_lessons = LessonSerializer(module_lessons, many=True, context={'request': request})
        return Response(serialized_lessons.data)
    except Module.DoesNotExist:
        return Response({"error": "Module does not exist."},
                        status=status.HTTP_404_NOT_FOUND)
def index(request):
       return render(request, 'index.html',{})






