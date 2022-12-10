from rest_framework.viewsets import ModelViewSet

from course.models import Course, EducationalMaterials, CourseStudents
from course.serializers import EMaterialsSerializer, CourseStudentsSerilalizer, CourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.mentor.user)


class EMaterialsViewSet(ModelViewSet):
    queryset = EducationalMaterials.objects.all()
    serializer_class = EMaterialsSerializer


class CourseStudentsViewSet(ModelViewSet):
    queryset = CourseStudents.objects.all()
    serializer_class = CourseStudentsSerilalizer
