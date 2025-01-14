from rest_framework.views import APIView, Request, Response, status
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404

from .serializers import MovieSerializer, MovieOrderSerializer
from .models import Movie
from movies.permissions import IsEmployeeOrReadOnly


class CustomPageNumberPagination(PageNumberPagination):  # Paginação customizada
    page_size = 2  # Quantidade de filmes por página
    page_size_query_param = 'page_size'
    max_page_size = 100


class MovieView(ListAPIView):  # View genérica para listagem com paginação
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = CustomPageNumberPagination
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployeeOrReadOnly]


class MovieDetailView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployeeOrReadOnly]

    def get(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MovieOrderDetailView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, req: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        movie_order = MovieOrderSerializer(data=req.data)
        movie_order.is_valid(raise_exception=True)
        movie_order.save(user_order=req.user, movie_order=movie)
        return Response(movie_order.data, status.HTTP_201_CREATED)
