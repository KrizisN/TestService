# Generated by Django 3.1.1 on 2020-10-13 15:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Test_kits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtest_test', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', models.CharField(max_length=300, verbose_name='Вопрос')),
                ('right_answer', models.BooleanField(blank=True, default=False, verbose_name='Правильный вопрос')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Test.test_kits')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='profile_images/', verbose_name='Изображение')),
                ('phone', models.IntegerField(blank=True, verbose_name='Телефоный номер')),
                ('man_or_woman', models.CharField(blank=True, choices=[('Мужчина', 'Мужчина'), ('Женщина', 'Женщина')], max_length=100, verbose_name='Пол')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
