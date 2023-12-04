# Импорт в файле, где объявлена модель Test
from django.db.models.signals import post_save
from django.dispatch import receiver

from app.myapi.models import Test


@receiver(post_save, sender=Test)
def update_module_tests(sender, instance, created, **kwargs):
    if created:
        module = instance.lesson.module
        module.update_number_of_tests()
        print("access!")
