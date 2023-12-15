from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)
router.register(r'courses', views.CourseViewSet)
router.register(r'modules', views.ModuleViewSet)
router.register(r'lessons', views.LessonViewSet)
router.register(r'tests', views.TestViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'answers', views.AnswerViewSet)



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('theory_files/<str:filename>/', views.theory_view_function, name='file-view'),
    path('images/<str:filename>/', views.images_view_function, name='file-view'),

]