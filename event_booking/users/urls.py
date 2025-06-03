from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView

urlpatterns = [
    path('sign-up/', RegisterView.as_view()),
    path('sign-in/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
]
