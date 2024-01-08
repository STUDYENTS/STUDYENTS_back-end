from django.urls import include, path
from rest_framework import routers
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import modules_for_course, lessons_for_module

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)
router.register(r'courses', views.CourseViewSet)
router.register(r'modules', views.ModuleViewSet)
router.register(r'lessons', views.LessonViewSet)
router.register(r'tests', views.TestViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'answers', views.AnswerViewSet)

urlpatterns = [
    path('front', views.index, name='index'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('theory_files/<str:filename>/', views.theory_view_function, name='file-view'),
    path('images/<str:filename>/', views.images_view_function, name='file-view'),
    path('img_course/<str:filename>/', views.images_course_view_function, name='file-view'),
    path('video/<str:filename>/', views.video_view_function, name='video-view'),
    path('modules_for_course/<int:course_id>/', modules_for_course, name='modules_for_course'),
    path('lessons_for_module/<int:module_id>/', lessons_for_module, name='lessons_for_module')
]
