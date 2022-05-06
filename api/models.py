from django.db import models
from django.db.models import Avg

from api.managers import IsAdultContentManagerMixin
from api.mixins import TimestampMixin, IsAdultContentModelMixin, NotDeletableModelMixin
from cms import settings
from utils.validators import validate_size, validate_extension


class Category(TimestampMixin):
    name = models.CharField(max_length=200)
    icon = models.ImageField(
        upload_to='images/category/',
        null=True,
        blank=True,
        validators=[validate_size, validate_extension],

    )
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.id}: {self.name}'


class Item(TimestampMixin, IsAdultContentModelMixin):
    name = models.CharField(max_length=200)
    price = models.FloatField(default=0.0)
    rating = models.FloatField(default=0.0)
    rating_count = models.IntegerField(default=0)
    short_description = models.TextField(blank=True)
    full_description = models.TextField(blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.DO_NOTHING,
        null=True,
        related_name='items'
    )

    objects = IsAdultContentManagerMixin()

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return f'{self.id}: {self.name} | {self.price}'

    def recalculate_rating(self):
        ratings = self.reviews
        print('rating saved')
        value = 0
        if ratings.exists():
            value = ratings.aggregate(avg=Avg('rating'))['avg']
        self.rating_count = ratings.count()
        self.rating = value
        self.save()


class Image(TimestampMixin):
    item = models.ForeignKey(Item,
                             on_delete=models.DO_NOTHING,
                             null=True,
                             related_name='images')
    name = models.CharField(max_length=64,
                            null=True,
                            blank=True)
    image = models.ImageField(
        upload_to='images/products/',
        validators=[validate_size, validate_extension],
        blank=True,
        null=True,
        verbose_name='Картинка'
    )

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return f'image {self.id}'


class Review(TimestampMixin):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name='reviews'
    )
    item = models.ForeignKey(
        Item,
        on_delete=models.SET_NULL,
        related_name='reviews',
        null=True
    )
    content = models.TextField()
    rating = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'review {self.id}'


class Order(TimestampMixin, NotDeletableModelMixin):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name='orders'
    )
    total_price = models.FloatField(default=0.0)

    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупка'

    def __str__(self):
        return f'review {self.id} | {self.total_price}'


class OrderItem(NotDeletableModelMixin):
    order = models.ForeignKey(
        Order,
        on_delete=models.DO_NOTHING,
        related_name='order_items'
    )
    item = models.ForeignKey(
        Item,
        on_delete=models.SET_NULL,
        related_name='order_items',
        null=True
    )
    count = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'Предмет покупки'
        verbose_name_plural = 'Предметы покупки'

    def __str__(self):
        return f'review {self.id} | {self.item.name} | {self.count}'
