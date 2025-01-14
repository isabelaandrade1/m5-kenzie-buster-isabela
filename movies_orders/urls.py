from django.urls import path
from .views import MovieOrderView

urlpatterns = [
    path("<int:movie_id>/orders/", MovieOrderView.as_view(), name="movie-order"),
]
