# Импорт в файле, где объявлена модель Test
from django.db.models.signals import post_save
from django.dispatch import receiver

from app.myapi.models import Test, Lesson, Module


@receiver(post_save, sender=Test)
def update_module_tests(sender, instance, created, **kwargs):
    if created:
        module = instance.lesson.module
        module.update_number_of_tests()
        print("access!")


@receiver(post_save, sender=Lesson)
def update_module_lessons(sender, instance, created, **kwargs):
    if created:
        module = instance.module
        module.update_number_of_lessons()
        print("access lesson!")


@receiver(post_save, sender=Lesson)
def update_course_lessons(sender, instance, created, **kwargs):
    if created:
        course = instance.course
        course.update_number_of_lessons()
        print("access lesson!")


@receiver(post_save, sender=Test)
def update_course_tests(sender, instance, created, **kwargs):
    if created:
        course = instance.course
        course.update_number_of_tests()
        print("access tests!")