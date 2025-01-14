from django.db import models
from django.conf import settings
from movies.models import Movie

class MovieOrder(models.Model):
    purchased_at = models.DateTimeField(auto_now_add=True)  # Data e hora do pedido
    price = models.DecimalField(max_digits=8, decimal_places=2)  # Preço com 2 casas decimais
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="movie_orders"
    )  # Relacionamento com usuários
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="movie_orders"
    )  # Relacionamento com filmes
