from django.db import models

from accounts.models import User, Student


class Course(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='courses',
                               verbose_name='Автор курса')
    title = models.CharField(max_length=100, verbose_name='Название курса')
    description = models.TextField(verbose_name='Описание')
    cover = models.ImageField(upload_to='Обложки курсов/%Y/%m/%d')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость курса')

    class Meta:
        verbose_name_plural = 'Курсы'
        verbose_name = 'Курс'

    def __str__(self):
        return f'{self.id}. {self.title}'


class EducationalMaterials(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='materials',
                               verbose_name='Материалы курса')
    subject = models.CharField(max_length=100, verbose_name='Тема')
    content = models.TextField(verbose_name='Содержание')
    file = models.FileField(upload_to='Файлы урока/%Y/%m/%d')
    link = models.URLField(verbose_name='Ссылка')

    def __str__(self):
        return f'{self.id}. {self.subject}'

    class Meta:
        verbose_name_plural = 'Материалы курса'
        verbose_name = 'Материал курса'


class CourseStudents(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='students', verbose_name='Курс')
    students = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='courses', verbose_name='Студент')

    def __str__(self):
        return f'{self.id}. {self.students}'

    class Meta:
        verbose_name_plural = 'Студенты курса'
        verbose_name = 'Студента курса'
