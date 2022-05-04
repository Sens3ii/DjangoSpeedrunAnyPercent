from django.urls import path
from rest_framework.routers import DefaultRouter

from api.api.views import CategoryViewSet, ItemSearchView, ItemViewSet, ReviewViewSet, OrderViewSet, CategoryItemsView, \
    OrderMyView

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
    path(
        "categories/<int:pk>/items/",
        CategoryItemsView.as_view(),
        name="get items by category",
    ),
    path(r'items/search/', ItemSearchView.as_view()),
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
    path(
        "orders/",
        OrderViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }),
        name="get/create orders",
    ),
    path(r'orders/my/', OrderMyView.as_view()),
    path(
        "orders/<int:pk>/",
        OrderViewSet.as_view(
            {
                "get": "retrieve",
            }),
        name="get orders",
    ),
]

urlpatterns += router.urls
