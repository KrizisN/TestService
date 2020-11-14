from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date


class Profile(models.Model):
    SEX = (
        ('Мужчина', 'Мужчина'),
        ('Женщина', 'Женщина')
    )
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    image = models.ImageField('Изображение', upload_to='profile_images/', blank=True)
    phone = models.CharField('Телефоный номер',max_length=30 ,null=True, blank=True)
    man_or_woman = models.CharField('Пол',max_length=100, blank=True, choices=SEX)
    date_created = models.DateField(auto_now_add=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return str(self.user)


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Test_kits(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE,null=True)
    subtest_test = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.subtest_test


class Test(models.Model):
    test_kits = models.ForeignKey(Test_kits, on_delete=models.CASCADE)
    questions = models.CharField('Вопрос', max_length=300)

    def get_absolute_url(self):
        return reverse("beer_detail", kwargs={"str": self.test})

    def __str__(self):
        return f"{self.test_kits}-{self.questions}"


class Answer(models.Model):
    question = models.ForeignKey(Test, on_delete=models.CASCADE, null=True)
    answer = models.CharField(max_length=400, null=True)
    right_answer = models.BooleanField('Правильный ответ', blank=True, default=False)

    def __str__(self):
        return f"{self.question}-{self.answer}"


class UsersTest(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    test_kits = models.ForeignKey(Test, on_delete=models.CASCADE, null=True)
    usersanswer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.user}-{self.test_kits}-{self.usersanswer}"


class UsersResults(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    test_kits = models.ForeignKey(Test_kits, on_delete=models.CASCADE)
    all_tests = models.IntegerField()
    right_tests = models.IntegerField()

    def __str__(self):
        return f"{self.user}-{self.test_kits}"