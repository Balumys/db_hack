import random

from datacenter.models import Schoolkid, Mark, Chastisement, Lesson, Commendation

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


def get_student(schoolkid):
    try:
        student = Schoolkid.objects.get(full_name__contains=schoolkid)
        return student
    except Schoolkid.DoesNotExist as err:
        return print(err)
    except Schoolkid.MultipleObjectsReturned as err:
        return print(f"{err} Specify exact name")


def fix_marks(schoolkid):
    student = get_student(schoolkid)
    Mark.objects.filter(schoolkid=student, points__in=[2, 3]).update(points=5)


def remove_chastisements(schoolkid):
    student = get_student(schoolkid)
    chastisement = Chastisement.objects.filter(schoolkid=student)
    chastisement.delete()


def create_commendation(subject, schoolkid):
    student = get_student(schoolkid)
    lesson = Lesson.objects.filter(subject__title=subject, subject__year_of_study=student.year_of_study).order_by(
        "-date").first()
    if lesson is None:
        return print("Cannot find lesson, check typos in subject name")
    commendation = Commendation.objects.create(text=random.choice(COMMENDATION_EXAMPLES), created=lesson.date,
                                               schoolkid=student, subject=lesson.subject, teacher=lesson.teacher)
