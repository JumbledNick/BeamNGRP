from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.conf import settings
from .models import Business, Profile, Wallet

@receiver(pre_delete, sender=Business)
def revert_business_owner(sender, instance, **kwargs):
    user = instance.owner

    if not hasattr (user, 'business'):
        user.role = 'user'
        user.save()

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_extras(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        Wallet.objects.create(user=instance)