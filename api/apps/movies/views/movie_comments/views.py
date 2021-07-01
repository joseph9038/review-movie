from django.db import transaction

from rest_framework.views import APIView
from rest_framework.exceptions import status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

from apps.common.model_loaders import (
    get_movie_model,
    get_genre_model,
    get_user_model,
    get_comment_model,
)
from apps.common.permissions import CustomPermission
from apps.movies.views.movie_comments.serializers import (
    CommentSerializer,
    PostMovieCommentSerializer,
    GetMovieCommentsSerializer,
)
from apps.common.responses import ApiMessageResponse
from apps.common.helpers import validate_data


def get_movie_id_for_movie_slug(movie_slug):
    Movie = get_movie_model()
    movie = Movie.objects.values("id").get(slug=movie_slug)
    return movie["id"]


class MovieComments(APIView):
    """
    The API for comments movie
    """

    permission_classes = (CustomPermission,)

    def get(self, request, movie_slug):
        data = validate_data(
            GetMovieCommentsSerializer, data={"movie_slug": movie_slug}
        )
        movie_slug = data.get("movie_slug")

        Movie = get_movie_model()
        comments = Movie.get_comments_with_movie_slug(movie_slug=movie_slug)
        comments_serializer = CommentSerializer(
            comments, many=True, context={"request": request}
        )
        return Response(comments_serializer.data, status=status.HTTP_200_OK)

    def post(self, request, movie_slug):
        request_data = self._get_request_data(request, movie_slug)

        data = validate_data(PostMovieCommentSerializer, request_data)
        movie_slug = data.get("movie_slug")
        content = data.get("content")

        user = request.user

        with transaction.atomic():
            movie_comment = user.comment_movie_with_slug(
                movie_slug=movie_slug, user=user, content=content
            )

        movie_comment_serializer = CommentSerializer(
            movie_comment, context={"request": request}
        )
        return Response(
            movie_comment_serializer.data, status=status.HTTP_201_CREATED
        )

    def _get_request_data(self, request, movie_slug):
        request_data = request.data.copy()
        query_params = request.query_params.dict()
        request_data.update(query_params)
        request_data["movie_slug"] = movie_slug
        return request_data


class CommentItem(APIView):
    """
    API for Get/Put/Delete comment item
    """

    permission_classes = (CustomPermission,)

    def get(self, request, comment_id):
        Comment = get_comment_model()
        try:
            movie = Comment.get_comment_with_id(comment_id)
            movie_serializer = CommentSerializer(
                movie, context={"request": request}
            )
            return Response(movie_serializer.data, status=status.HTTP_200_OK)
        except Comment.DoesNotExist:
            return ApiMessageResponse(
                "Comment not found", status=status.HTTP_404_NOT_FOUND
            )

    def patch(self, request, comment_id):
        return

    def delete(self, request, comment_id):
        return

    def _get_request_data(self, request, comment_id):
        request_data = request.data.copy()
        request_data["comment_id"] = comment_id
        return request_data
