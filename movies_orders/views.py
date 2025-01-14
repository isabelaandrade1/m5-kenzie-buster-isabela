from rest_framework.views import APIView, Request, Response, status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from movies.models import Movie
from .models import MovieOrder
from .serializers import MovieOrderSerializer

class MovieOrderView(APIView):
    permission_classes = [IsAuthenticated]  # Apenas usuários autenticados

    def post(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)  # Busca o filme pelo ID
        serializer = MovieOrderSerializer(data=request.data, context={"request": request, "movie": movie})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

