import random
import sys

from datacenter.models import Schoolkid, Mark, Chastisement, Lesson, Commendation
from django.core.exceptions import ObjectDoesNotExist

COMMENDATION_EXAMPLES = [
    "Молодец!",
    "Отлично!",
    "Хорошо!",
    "Гораздо лучше, чем я ожидал!",
    "Ты меня приятно удивил!",
    "Великолепно!",
    "Прекрасно!",
    "Ты меня очень обрадовал!",
    "Именно этого я давно ждал от тебя!",
    "Сказано здорово – просто и ясно!",
    "Ты, как всегда, точен!",
    "Очень хороший ответ!",
    "Талантливо!",
    "Ты сегодня прыгнул выше головы!",
    "Я поражен!",
    "Уже существенно лучше!",
    "Потрясающе!",
    "Замечательно!",
    "Прекрасное начало!",
    "Так держать!",
    "Ты на верном пути!",
    "Здорово!",
    "Это как раз то, что нужно!",
    "Я тобой горжусь!",
    "С каждым разом у тебя получается всё лучше!",
    "Мы с тобой не зря поработали!",
    "Я вижу, как ты стараешься!",
    "Ты растешь над собой!",
    "Ты многое сделал, я это вижу!",
    "Теперь у тебя точно все получится!"
]


def fix_marks(schoolkid):
    try:
        student = Schoolkid.objects.get(full_name__contains=schoolkid)
    except ObjectDoesNotExist as err:
        sys.exit(err)
    marks = Mark.objects.filter(schoolkid=student, points__in=[2, 3])
    for mark in marks:
        mark.points = 5
        mark.save()


def remove_chastisements(schoolkid):
    try:
        student = Schoolkid.objects.get(full_name__contains=schoolkid)
    except ObjectDoesNotExist as err:
        sys.exit(err)
    chastisement = Chastisement.objects.filter(schoolkid=student)
    chastisement.delete()


def create_commendation(subject, schoolkid):
    student = Schoolkid.objects.get(full_name__contains=schoolkid)
    lesson = Lesson.objects.filter(subject__title=subject, subject__year_of_study=student.year_of_study).order_by(
        "-date").first()
    if lesson is None:
        return print("Cannot find lesson, check typos in subject name")
    commendation = Commendation.objects.create(text=random.choice(COMMENDATION_EXAMPLES), created=lesson.date,
                                               schoolkid=student, subject=lesson.subject, teacher=lesson.teacher)
