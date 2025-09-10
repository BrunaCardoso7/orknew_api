from django.urls import path

from apps.users.views import UserViewSet

urlpatterns = [
    path(
        "api/users/me/",
        UserViewSet.as_view({"get": "get_current_user"}),
        name="users/me/",
    ),
    path(
        "api/users/",
        UserViewSet.as_view({"get": "list", "post": "create"}),
        name="users/",
    ),
    path(
        "api/users/<int:pk>/",
        UserViewSet.as_view(
            {"get": "retrieve", "patch": "update", "delete": "destroy"}
        ),
        name="users",
    ),
]
