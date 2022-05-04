from django.urls import path
from rest_framework.routers import DefaultRouter

from api.api.views import CategoryViewSet, CategorySearchView, ItemViewSet, ReviewViewSet

app_name = 'api'

router = DefaultRouter()

urlpatterns = [
    path(
        "categories/",
        CategoryViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }),
        name="get/create categories",
    ),
    path(
        "categories/<int:pk>/",
        CategoryViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                'delete': 'destroy'
            }),
        name="get/put category",
    ),
    path(r'categories/search/', CategorySearchView.as_view()),
    path(
        "items/",
        ItemViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }),
        name="get/create items",
    ),
    path(
        "items/<int:pk>/",
        ItemViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                'delete': 'destroy'
            }),
        name="get/put items",
    ),
    path(
        "reviews/",
        ReviewViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }),
        name="get/create reviews",
    ),
    path(
        "reviews/<int:pk>/",
        ReviewViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                'delete': 'destroy'
            }),
        name="get/put reviews",
    ),
]

urlpatterns += router.urls
