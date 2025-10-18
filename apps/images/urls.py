from django.urls import path

from apps.images.views import ImagesViewSet

urlpatterns = [
    path(
        "api/images/",
        ImagesViewSet.as_view({"get": "list", "post": "create"}),
        name="images/",
    ),
path(
        "api/images_profile/",
        ImagesViewSet.as_view({"post": "images_profile"}),
        name="images-profile/",
    ),
    path(
        "api/images/",
        ImagesViewSet.as_view(
            {"get": "retrieve", "patch": "update", "delete": "destroy"}
        ),
        name="images",
    ),
]
