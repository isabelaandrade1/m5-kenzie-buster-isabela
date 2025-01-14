from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import UserCreateView, UserDetailView

urlpatterns = [
    path('', UserCreateView.as_view(), name='user-create'),  
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path('<int:user_id>/', UserDetailView.as_view(), name='user-detail'), 
]
