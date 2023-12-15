from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Test, Task, Lesson


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


@receiver(post_save, sender=Lesson)
@receiver(post_delete, sender=Lesson)
def update_lesson_count(sender, instance, **kwargs):
    module = instance.module
    lesson_count = Lesson.objects.filter(module=module).count()
    module.number_of_lessons = lesson_count
    module.save()


@receiver(post_save, sender=Lesson)
@receiver(post_delete, sender=Lesson)
def update_lesson_count_in_course(sender, instance, **kwargs):
    module = instance.module
    course = module.course
    lesson_count = Lesson.objects.filter(module__course=course).count()
    course.number_of_lessons = lesson_count
    course.save()

@receiver(post_save, sender=Test)
@receiver(post_delete, sender=Test)
def update_test_count_in_course(sender, instance, **kwargs):
    lesson = instance.lesson
    module = lesson.module
    course = module.course
    test_count = Test.objects.filter(lesson__module__course=course).count()
    course.number_of_tests = test_count
    course.save()

