from django.urls import path, include
from rest_framework.routers import DefaultRouter

from course.views import *

router = DefaultRouter()
router.register('course', CourseViewSet)
router.register('materials', EMaterialsViewSet)
router.register('students', CourseStudentsViewSet)


urlpatterns = [
    path('', include(router.urls))
]