import logging

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from api.models import Review

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Review)
def rating_added(sender, instance, **kwargs):
    print("update rating updated")
    instance.item.recalculate_rating()


@receiver(post_delete, sender=Review)
def rating_deleted(sender, instance, **kwargs):
    print("delete rating updated")
    instance.item.recalculate_rating()
