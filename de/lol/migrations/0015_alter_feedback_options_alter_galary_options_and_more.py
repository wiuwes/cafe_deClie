# Generated by Django 4.0.1 on 2022-03-31 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lol', '0014_reservation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'verbose_name': 'Пожелание', 'verbose_name_plural': 'Пожелания'},
        ),
        migrations.AlterModelOptions(
            name='galary',
            options={'verbose_name': 'Фото', 'verbose_name_plural': 'Галерея'},
        ),
        migrations.AlterModelOptions(
            name='mp',
            options={'verbose_name': 'Мероприятие', 'verbose_name_plural': 'Мероприятия'},
        ),
        migrations.AlterModelOptions(
            name='regmp',
            options={'verbose_name': 'Зарегистрирувшийся на мероприятие', 'verbose_name_plural': 'Зарегистрирувшиеся на мероприятие'},
        ),
        migrations.AlterModelOptions(
            name='store',
            options={'verbose_name': 'Раздел еды', 'verbose_name_plural': 'Разделы еды'},
        ),
        migrations.AlterModelOptions(
            name='store_chapter',
            options={'verbose_name': 'Блюдо', 'verbose_name_plural': 'Блюда'},
        ),
        migrations.AlterModelOptions(
            name='vacance',
            options={'verbose_name': 'Вакансия', 'verbose_name_plural': 'Вакансии'},
        ),
        migrations.AlterField(
            model_name='reservation',
            name='place',
            field=models.CharField(max_length=30),
        ),
    ]