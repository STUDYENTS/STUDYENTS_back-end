from django.urls import include, path

from rest_framework import routers

router = routers.DefaultRouter()
urlpatterns = [

    path('front', include(router.urls)),


]