from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.accounts.views import (
    ObtainTokenPairWithColorView,
    Register,
    Logout,
    UserProfile,
)
from apps.movies.views import MovieItem, MovieRatings, RatingItem
from apps.comments.views import CommentItem, MovieComments
from apps.search import urls as search_index_urls


auth_auth_patterns = [
    path(
        "login",
        ObtainTokenPairWithColorView.as_view(),
        name="login-user",
    ),
    path("login/refresh", TokenRefreshView.as_view(), name="login-refresh"),
    path("logout", Logout.as_view(), name="logout-user"),
    path("register", Register.as_view(), name="register-user"),
]

auth_users_patterns = [
    path("<int:user_id>", UserProfile.as_view(), name="user"),
]

auth_patterns = [
    path("", include(auth_auth_patterns)),
    path("users/", include(auth_users_patterns)),
]


movie_patterns = [
    path("", MovieItem.as_view(), name="movie"),
    path("comments", MovieComments.as_view(), name="movie-comments"),
    path("ratings", MovieRatings.as_view(), name="movie-ratings"),
]

movies_patterns = [
    path("<int:movie_id>/", include(movie_patterns)),
]

ratings_patterns = [
    path("<int:rating_id>", RatingItem.as_view(), name="rating-item"),
]

comments_patterns = [
    path("<int:comment_id>", CommentItem.as_view(), name="comment-item"),
]

api_patterns = [
    path("auth/", include(auth_patterns)),
    path("movies/", include(movies_patterns)),
    path("ratings/", include(ratings_patterns)),
    path("comments/", include(comments_patterns)),
    path("search/", include(search_index_urls)),
]

urlpatterns = [
    path("api/", include(api_patterns)),
    path("admin/", admin.site.urls),
]
