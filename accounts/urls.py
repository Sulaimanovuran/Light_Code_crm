from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import *

router = DefaultRouter()
router.register('user', UserViewSet)
router.register('score', ScoreView)
router.register('leeds', LeedViewSet)

app_name = 'users'

urlpatterns = [
    path('register/mentor/', RegisterMentorAPIView.as_view()),
    path('register/student/', RegisterStudentAPIView.as_view()),
    path('user/student/', UserRetrieveAPIView.as_view()),
    path('student/getscores/', ScorelListAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogOutApiView.as_view()),
]
