from django.db import models


class NotDeletableManagerMixin(models.Manager):
    DELETE_FIELD = 'is_deleted'

    def filter(self, with_deleted=False, *args, **kwargs):
        if with_deleted:
            super().filter(*args, **kwargs)
        if self.DELETE_FIELD not in kwargs:
            kwargs[self.DELETE_FIELD] = False
        return super().filter(*args, **kwargs)

    def exclude(self, with_deleted=False, *args, **kwargs):
        if with_deleted:
            super().exclude(*args, **kwargs)
        if self.DELETE_FIELD not in kwargs:
            kwargs[self.DELETE_FIELD] = False
        return super().exclude(*args, **kwargs)

    def all(self, with_deleted=False):
        if not with_deleted:
            return super().filter(is_deleted=False)
        return super().all()

    def get(self, with_deleted=False, *args, **kwargs):
        if with_deleted:
            super().filter(*args, **kwargs)
        if self.DELETE_FIELD not in kwargs:
            kwargs[self.DELETE_FIELD] = False
        return super().get(*args, **kwargs)


class IsAdultContentManagerMixin(models.Manager):
    IS_ADULT_CONTENT_FIELD = 'is_adult_content'

    def filter(self, with_adult=False, *args, **kwargs):
        if with_adult:
            super().filter(*args, **kwargs)
        if self.IS_ADULT_CONTENT_FIELD not in kwargs:
            kwargs[self.IS_ADULT_CONTENT_FIELD] = False
        return super().filter(*args, **kwargs)

    def exclude(self, with_adult=False, *args, **kwargs):
        if with_adult:
            super().exclude(*args, **kwargs)
        if self.IS_ADULT_CONTENT_FIELD not in kwargs:
            kwargs[self.IS_ADULT_CONTENT_FIELD] = False
        return super().exclude(*args, **kwargs)

    def all(self, with_adult=False):
        if not with_adult:
            return super().filter(is_adult_content=False)
        return super().all()

    def get(self, with_adult=False, *args, **kwargs):
        if with_adult:
            super().filter(*args, **kwargs)
        if self.IS_ADULT_CONTENT_FIELD not in kwargs:
            kwargs[self.IS_ADULT_CONTENT_FIELD] = False
        return super().get(*args, **kwargs)
