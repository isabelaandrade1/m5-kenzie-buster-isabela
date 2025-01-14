from rest_framework import serializers
from .models import MovieOrder

class MovieOrderSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source="movie.title", read_only=True)  # Título do filme
    purchased_by = serializers.EmailField(source="user.email", read_only=True)  # Email do comprador

    class Meta:
        model = MovieOrder
        fields = ['id', 'title', 'purchased_at', 'price', 'purchased_by']

    def create(self, validated_data):
        user = self.context['request'].user  # Usuário autenticado
        movie = self.context['movie']  # Filme passado na rota
        return MovieOrder.objects.create(**validated_data, user=user, movie=movie)
