from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import Leed


@receiver(post_save, sender=Leed)
def post_save_leed(created, **kwargs):
    try:
        if not created:
            instance = kwargs['instance']
            if instance.enrolled:
                Leed.objects.get(id=instance.id).delete()
    except:
        pass
