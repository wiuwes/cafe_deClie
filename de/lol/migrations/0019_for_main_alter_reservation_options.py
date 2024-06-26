# Generated by Django 4.0.1 on 2022-04-01 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lol', '0018_alter_reservation_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='for_main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='for_main')),
                ('color_background', models.CharField(max_length=20)),
                ('colot_text', models.CharField(max_length=20)),
                ('text', models.TextField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='reservation',
            options={'verbose_name': 'Забронированный столик', 'verbose_name_plural': 'Забронированные столики'},
        ),
    ]
