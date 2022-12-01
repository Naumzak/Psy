from django.db import models

# Create your models here.
from django.db import models


class Results(models.Model):
    sex = models.CharField(max_length=50)
    education = models.CharField(max_length=50)
    work = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    answer1 = models.CharField(max_length=50)
    answer2 = models.CharField(max_length=50)
    answer3 = models.CharField(max_length=50)
    answer4 = models.CharField(max_length=50)
    answer5 = models.CharField(max_length=50)
    answer6 = models.CharField(max_length=50)
    answer7 = models.CharField(max_length=50)
    answer8 = models.CharField(max_length=50)
    answer9 = models.CharField(max_length=50)
    answer10 = models.CharField(max_length=50)
    answer11 = models.CharField(max_length=50)
    answer12 = models.CharField(max_length=50)
    answer13 = models.CharField(max_length=50)
    answer14 = models.CharField(max_length=50)
    answer15 = models.CharField(max_length=50)
    answer16 = models.CharField(max_length=50)
    answer17 = models.CharField(max_length=50)
    answer18 = models.CharField(max_length=50)
    answer19 = models.CharField(max_length=50)
    answer20 = models.CharField(max_length=50)
    answer21 = models.CharField(max_length=50)
    answer22 = models.CharField(max_length=50)
    answer23 = models.CharField(max_length=50)
    answer24 = models.CharField(max_length=50)
    answer25 = models.CharField(max_length=50)
    answer26 = models.CharField(max_length=50)
    answer27 = models.CharField(max_length=50)
    answer28 = models.CharField(max_length=50)
    answer29 = models.CharField(max_length=50)
    answer31 = models.CharField(max_length=50)
    answer32 = models.CharField(max_length=50)
    answer33 = models.CharField(max_length=50)
    answer34 = models.CharField(max_length=50)
    answer35 = models.CharField(max_length=50)


class Answers(models.Model):
    answer = models.CharField(max_length=50)

    def __str__(self):
        return self.answer


class Quests(models.Model):
    text = models.CharField(max_length=1000)
    type_quest = models.CharField(max_length=50)
    answers = models.ManyToManyField(Answers, blank=True, )
    right_answer = models.CharField(max_length=50)
    image = models.ImageField(upload_to='img/', blank=True, null=True)
    timer = models.BooleanField()
    timer_time = models.PositiveIntegerField(blank=True, null=True)
    number = models.PositiveIntegerField(unique=True)
    factor = models.PositiveIntegerField()

    def get_image(self):
        try:
            return self.image.url
        except:
            return None

    def __str__(self):
        return self.text
