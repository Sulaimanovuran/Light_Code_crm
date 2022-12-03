from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import User, Score, Leed
from .serializers import *


class RegisterMentorAPIView(generics.ListCreateAPIView):
    '''Регистрация ментора'''
    queryset = User.objects.all()
    serializer_class = RegisterMentorSerializer

    # @decorators.action(['GET'], detail=False)
    # def list(self, request):
    #     res = User.objects.all()
    #     return Response(RegisterClientSerializer(res, many=True).data)


class RegisterStudentAPIView(generics.ListCreateAPIView):
    '''Регистрация студента'''
    queryset = User.objects.all()
    serializer_class = RegisterStudentSerializer


class LoginApiView(ObtainAuthToken):
    '''Авторизация'''
    serializer_class = LoginSerializer


class LogOutApiView(APIView):
    '''Выход из системы'''
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            user = request.user
            Token.objects.filter(user=user).delete()
            return Response('Вы успешно разлогинились')
        except Exception as s:
            print('*********', s, '****************')
            return Response(status=403)


class UserViewSet(ModelViewSet):
    '''VIEW для ментора'''
    queryset = User.objects.all()
    serializer_class = UserMentorSerializer


class UserRetrieveAPIView(generics.ListAPIView):
    '''VIEW для студента'''
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(code=user.student.code)


class ScorelListAPIView(generics.ListAPIView):
    '''Просмотр оценок для студента'''
    serializer_class = ScoreSerializer

    def get_queryset(self):
        user = self.request.user
        return Score.objects.filter(student_id=user.student.id)


class ScoreView(ModelViewSet):
    '''Создание оценок для ментора'''
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer


class LeedViewSet(ModelViewSet):
    '''Лиды для менеджера'''
    queryset = Leed.objects.all()
    serializer_class = LeedMentorSerializer


class LeedListCreateAPIView(generics.ListCreateAPIView):
    '''Для потенциальных студентов'''
    queryset = Leed.objects.all()
    serializer_class = LeedSerializer
