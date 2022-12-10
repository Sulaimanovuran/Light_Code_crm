from rest_framework import serializers

from accounts.models import Student
from course.models import Course, EducationalMaterials, CourseStudents


class CourseStudentsSerilalizer(serializers.ModelSerializer):
    class Meta:
        model = CourseStudents
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.full_name')
    students = CourseStudentsSerilalizer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        course = Course.objects.create(**validated_data)
        if 'students' in request.data.dict().keys():
            students = request.POST.getlist('students')
            for student in students:
                CourseStudents.objects.create(course=course, students=Student.objects.get(id=int(student)))

        return course


class EMaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalMaterials
        fields = '__all__'
