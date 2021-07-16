from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineProduct


@receiver(post_save, sender=OrderLineProduct)
# sender of the signal, instance of the model that sent it,
# boolen sent by django to confirm if this is a new instance or being updated
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on line product update/create
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineProduct)
def update_on_save(sender, instance, **kwargs):
    """
    Update order total on line product delete
    """
    instance.order.update_total()
