# Generated by Django 4.0.4 on 2022-05-22 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('STR', '0008_alter_schedule_time_range_alter_schedule_weekday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='time_range',
            field=models.IntegerField(choices=[('C 8:00 до 9:30', 1), ('С 9:45 до 11:15', 2), ('С 11:30 до 13:15', 3), ('С 13:30 до 15:00', 4), ('С 15:15 до 16:45', 5), ('С 17:00 до 18:30', 6)], default=1, max_length=40, verbose_name='Время'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='weekday',
            field=models.IntegerField(choices=[('Понедельник', 1), ('Вторник', 2), ('Среда', 3), ('Четверг', 4), ('Пятница', 5), ('Суббота', 6)], default=1, max_length=20, verbose_name='День недели'),
        ),
    ]
