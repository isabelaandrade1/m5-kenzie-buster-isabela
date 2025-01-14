from django.urls import path
from .views import MovieView, MovieDetailView, MovieOrderDetailView

urlpatterns = [
    path("", MovieView.as_view(), name="movie-list-create"),  # Listar e criar filmes
    path("<int:movie_id>/", MovieDetailView.as_view(), name="movie-detail"),  # Detalhes de filme
    path("<int:movie_id>/orders/", MovieOrderDetailView.as_view(), name="movie-order"),  # Criar pedido de filme
]
