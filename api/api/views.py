from rest_framework import generics, mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.api.serializers import CategoryBaseSerializer, ItemBaseSerializer, ItemListResponseSerializer, \
    ItemRetrieveResponseSerializer, CommentBaseSerializer, CommentGetSerializer, CommentUpdateSerializer
from api.models import Category, Item, Review
from cms.permissions import IsOwnerOrReadOnly


class CategoryViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin
):
    queryset = Category.objects.all()
    serializer_class = CategoryBaseSerializer
    permission_classes = [IsAuthenticated]


class CategorySearchView(
    APIView
):
    queryset = Category.objects.all()
    serializer_class = CategoryBaseSerializer
    permission_classes = [IsAuthenticated]

    @action(methods=["GET"], detail=False)
    def get(self, request):
        search = self.request.query_params.get('search', None)
        if search:
            queryset = self.queryset.filter(name__icontains=search)
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response([], status=status.HTTP_200_OK)


class ItemViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin
):
    queryset = Item.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return ItemListResponseSerializer
        if self.action == 'retrieve':
            return ItemRetrieveResponseSerializer
        return ItemBaseSerializer


class ReviewViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin
):
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return CommentGetSerializer
        if self.action == 'update':
            return CommentUpdateSerializer
        return CommentBaseSerializer
