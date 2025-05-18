from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, SubTaskViewSet, DateViewSet
from . import views

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task') 
router.register(r'subtasks', SubTaskViewSet, basename='subtask')
router.register(r'dates', DateViewSet, basename='date')
urlpatterns = [
    path('', include(router.urls)),
    path('', views.api_root),
]