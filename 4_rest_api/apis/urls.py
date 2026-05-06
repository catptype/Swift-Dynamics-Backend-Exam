from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.v1.school import SchoolViewSet
from .views.v1.classroom import ClassroomViewSet
from .views.v1.teacher import TeacherViewSet
from .views.v1.student import StudentViewSet

router = DefaultRouter()
router.register(r'schools', SchoolViewSet, basename='school')
router.register(r'classrooms', ClassroomViewSet, basename='classroom')
router.register(r'teachers', TeacherViewSet, basename='teacher')
router.register(r'students', StudentViewSet, basename='student')

urlpatterns = [
    path('v1/', include(router.urls)),
]