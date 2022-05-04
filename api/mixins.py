from gettext import gettext

from django.db import models


class TimestampMixin(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время последнего изменения')


class NotDeletableModelMixin(models.Model):
    DELETE_FIELD = 'is_deleted'

    class Meta:
        abstract = True

    is_deleted = models.BooleanField(default=False)

    def delete(self, using=None, *args, **kwargs):
        setattr(self, self.DELETE_FIELD, True)
        self.save(using=using, update_fields=[self.DELETE_FIELD])

    def __str__(self):
        if getattr(self, self.DELETE_FIELD):
            return gettext("DELETED ")
        return ""


class IsAdultContentModelMixin(models.Model):
    IS_ADULT_CONTENT_FIELD = 'is_adult_content'

    class Meta:
        abstract = True

    is_adult_content = models.BooleanField(default=False)
