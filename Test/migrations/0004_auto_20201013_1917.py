# Generated by Django 3.1.1 on 2020-10-13 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0003_auto_20201013_1908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='right_answer',
        ),
        migrations.AlterField(
            model_name='userstest',
            name='test_kits',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Test.test'),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('right_answer', models.BooleanField(blank=True, default=False, verbose_name='Правильный вопрос')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Test.test')),
            ],
        ),
    ]
