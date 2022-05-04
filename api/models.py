from django.db import models

from utils.validators import validate_size, validate_extension


class TimestampMixin(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время последнего изменения')


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


class Item(TimestampMixin):
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

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return f'{self.id}: {self.name} | {self.price}'


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
        return f'{self.id}'
