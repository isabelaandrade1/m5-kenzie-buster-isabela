from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import UserCreateView

urlpatterns = [
    path('', UserCreateView.as_view(), name='user-create'),  # Rota para criar usuário
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Rota para login
]
