# Generated by Django 4.0.4 on 2022-05-22 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('STR', '0009_alter_schedule_time_range_alter_schedule_weekday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='subgroup_number',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 1), (2, 2)], default=None, null=True, verbose_name='Подгруппа'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='time_range',
            field=models.PositiveSmallIntegerField(choices=[(1, 'C 8:00 до 9:30'), (2, 'С 9:45 до 11:15'), (3, 'С 11:30 до 13:15'), (4, 'С 13:30 до 15:00'), (5, 'С 15:15 до 16:45'), (6, 'С 17:00 до 18:30')], default=1, verbose_name='Время'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='weekday',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Понедельник'), (2, 'Вторник'), (3, 'Среда'), (4, 'Четверг'), (5, 'Пятница'), (6, 'Суббота')], default=1, verbose_name='День недели'),
        ),
    ]
