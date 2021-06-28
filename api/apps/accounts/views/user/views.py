from django.db import DatabaseError, transaction
from django.shortcuts import render
from django.core.paginator import Paginator

from rest_framework import status
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView


from apps.accounts.views.user.serializers import (
    GetUserDataSerializer,
    UserInfoSerializer,
    UserRatingsSerializer,
    UserCommentsSerializer,
    AuthenticatedUserInfoSerializer,
    DeleteAuthenticatedUserSerializer,
)
from apps.common.model_loaders import (
    get_movie_model,
    get_rating_model,
    get_user_model,
    get_comment_model,
)
from apps.common.permissions import CustomPermission
from apps.accounts.models import User
from apps.common.helpers import validate_data
from apps.common.pagination import SmallResultsSetPagination
from apps.common.responses import ApiMessageResponse


class GetUserInfo(APIView):
    """[summary]

    Args:
        APIView ([type]): [description]
    """

    def get(self, request, username):
        request_data = request.data.copy()
        request_data["username"] = username

        data = validate_data(GetUserDataSerializer, request_data)
        username = data.get("username")

        user = request.user

        if user.username == username:
            target_user = user
        else:
            target_user = User.get_user_with_username(username=username)

        user_serializer = UserInfoSerializer(
            target_user, context={"request": request}
        )

        return Response(user_serializer.data, status=status.HTTP_200_OK)


class UserRatings(ListAPIView):
    """[summary]

    Args:
        ListAPIView ([type]): [description]

    Returns:
        [type]: [description]
    """

    serializer_class = UserRatingsSerializer
    pagination_class = SmallResultsSetPagination
    queryset = get_rating_model().objects.all()

    def get_queryset(self):
        qs = super(UserRatings, self).get_queryset()

        username = self.kwargs.get("username")
        if username is not None:
            return qs.filter(user__username=username)

        return qs


class UserComments(ListAPIView):
    """[summary]

    Args:
        APIView ([type]): [description]

    Returns:
        [type]: [description]
    """

    serializer_class = UserCommentsSerializer
    pagination_class = SmallResultsSetPagination
    queryset = get_comment_model().objects.all()

    def get_queryset(self):
        qs = super(UserComments, self).get_queryset()

        username = self.kwargs.get("username")
        if username is not None:
            return qs.filter(user__username=username)

        return qs


class AuthenticatedUser(APIView):
    """[summary]

    Args:
        APIView ([type]): [description]

    Returns:
        [type]: [description]
    """

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user_serializer = AuthenticatedUserInfoSerializer(
            request.user, context={"request": request}
        )
        return Response(user_serializer.data, status=status.HTTP_200_OK)

    # def patch(self, request):
    # serializer = UpdateAuthenticatedUserSerializer(data=request.data)
    # serializer.is_valid(raise_exception=True)
    # data = serializer.validated_data

    # user = request.user

    # with transaction.atomic():
    #     user.update(
    #         username=data.get("username"),
    #         email=data.get("email"),
    #         birthday=data.get("birthday"),
    #         gender=data.get("gender"),
    #         save=False,
    #     )

    #     has_avatar = "avatar" in data
    #     if has_avatar:
    #         avatar = data.get("avatar")
    #         if avatar is None:
    #             user.delete_avatar(save=False)
    #         else:
    #             user.update_avatar(avatar, save=False)

    #     user.save()

    # user_serializer = UserInfoSerializer(
    #     user, context={"request": request}
    # )
    # return Response(user_serializer.data, status=status.HTTP_200_OK)


class DeleteAuthenticatedUser(APIView):
    """[summary]

    Args:
        APIView ([type]): [description]
    """

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = validate_data(DeleteAuthenticatedUserSerializer, request.data)

        user = request.user
        password = data.get("password")

        with transaction.atomic():
            user.delete_with_password(password=password)

        return ApiMessageResponse("Goodbye 😔", status=status.HTTP_200_OK)


class AuthenticatedUserSetting(APIView):
    """[summary]

    Args:
        APIView ([type]): [description]
    """

    permission_classes = (IsAuthenticated,)

    def __init__(self, *args):
        return
