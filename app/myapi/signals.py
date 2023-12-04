from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Test, Task


@receiver(post_save, sender=Test)
@receiver(post_delete, sender=Test)
def update_module_test_count(sender, instance, **kwargs):
    module = instance.lesson.module
    module.update_number_of_tests()

@receiver(post_save, sender=Task)
@receiver(post_delete, sender=Task)
def update_test_task_count(sender, instance, **kwargs):
    test = instance.test
    task_count = Task.objects.filter(test=test).count()
    test.number_of_tasks = task_count
    test.save()
